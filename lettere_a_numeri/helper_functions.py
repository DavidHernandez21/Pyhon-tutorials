import re
from collections import OrderedDict
from itertools import chain
from pickle import load
from typing import List

from yaml import safe_load


def unpickle_file(file_path: str):
    with open(file_path, 'br') as f:
        return load(f)


def _letters_to_numbers(
    ord_dict: OrderedDict[str, int],
    findall_list: List,
    count: int = 1,
    to_replace: str = '0',
    second_replace: bool = False,
    wo_replace: bool = False,
    **args,
) -> str:
    if wo_replace:
        return ''.join(str(ord_dict[f]) for f in findall_list)

    if not second_replace:
        return ''.join(
            str(ord_dict[f]).replace(to_replace, '', count) for f in findall_list
        )

    assert isinstance(
        args.get('count2', 100),
        int,
    ), "argument 'count2' must be an integer"

    return ''.join(
        str(ord_dict[f])
        .replace(to_replace, '', count)
        .replace(args.get('rep2', '1'), '', args.get('count2', 100))
        for f in findall_list
    )


def letters_to_numbers(
    pattern: re.Pattern,
    st: str,
    ord_dict: OrderedDict[str, int],
    duecento_novecento: List,
) -> str:
    findall = re.findall(pattern, st)
    le = len(findall)

    if le == 1:
        return str(ord_dict[findall[0]])

    if le == 2:
        if st in duecento_novecento:
            return str(duecento_novecento[st])

        if 'cento' not in findall or st.endswith('tuno') or st.endswith('otto'):
            return _letters_to_numbers(ord_dict, findall, count=100, to_replace='0')

        else:
            if st.endswith('nta') or st.endswith('nti'):
                return re.sub(
                    r'0',
                    '',
                    _letters_to_numbers(ord_dict, findall, wo_replace=True),
                    count=2,
                )

            else:
                return _letters_to_numbers(ord_dict, findall, count=1, to_replace='0')

    if le == 3:
        if findall[0] == 'cento':
            return _letters_to_numbers(ord_dict, findall, count=100, to_replace='0')
        else:
            if st.endswith('nta') or st.endswith('nti'):
                return re.sub(
                    r'[01]',
                    '',
                    _letters_to_numbers(ord_dict, findall, wo_replace=True),
                    count=3,
                )

            elif not (
                st.endswith('ici')
                or st.endswith('ette')
                or st.endswith('otto')
                or st.endswith('annove')
                or st.endswith('tuno')
            ):
                return _letters_to_numbers(
                    ord_dict,
                    findall,
                    count=1,
                    to_replace='0',
                    second_replace=True,
                    rep2='1',
                    count2=100,
                )

            elif st.endswith('tuno'):
                return re.sub(
                    r'1',
                    '',
                    _letters_to_numbers(ord_dict, findall, count=100, to_replace='0'),
                    count=1,
                )

            else:
                return re.sub(
                    '1',
                    '',
                    _letters_to_numbers(ord_dict, findall, count=2, to_replace='0'),
                    count=1,
                )

    if le == 4:
        return _letters_to_numbers(
            ord_dict,
            findall,
            count=100,
            to_replace='0',
            second_replace=True,
            rep2='1',
            count2=100,
        )


def split_and_yield(
    pattern: re.Pattern,
    st: str,
    ord_dict: OrderedDict[str, int],
    duecento_novecento: List,
):
    for ww in pattern.findall(st):
        yield letters_to_numbers(
            pattern=pattern,
            st=ww,
            ord_dict=ord_dict,
            duecento_novecento=duecento_novecento,
        )


def separate_numeric_yield(
    pattern: re.Pattern,
    st: str,
    ord_dict: OrderedDict[str, int],
    duecento_novecento: List,
    letter_num_pattern: re.Pattern,
):
    for g in filter(None, chain.from_iterable(letter_num_pattern.findall(st))):
        if g.isnumeric():
            yield g

        else:
            for ww in split_and_yield(
                pattern=pattern,
                st=g,
                ord_dict=ord_dict,
                duecento_novecento=duecento_novecento,
            ):
                yield ww


def list_tuples_finditer(
    pattern_attached: re.Pattern,
    pattern_nta_nti: re.Pattern,
    pattern_200_900: re.Pattern,
    st: str,
):
    found_first_character = False

    v = []

    for f in pattern_attached.finditer(st):
        if f.span()[0] == 0:
            found_first_character = True
        v.append((f.span(), f.group(), False))

    new_s = pattern_attached.sub(lambda x: '#' * len(x.group()), st)

    for f in pattern_nta_nti.finditer(new_s):
        if f.span()[0] == 0:
            found_first_character = True
        v.append((f.span(), f.group(), False))

    new_s = pattern_nta_nti.sub(lambda x: '#' * len(x.group()), new_s)

    for f in pattern_200_900.finditer(new_s):
        if f.span()[0] == 0:
            found_first_character = True
        v.append((f.span(), f.group(), False))

    v = sorted(v, key=lambda x: x[0][0])
    le = len(v)
    for i, k in enumerate(v, 1):
        if i < le and k[0][1] == v[i][0][0]:
            v[i] = (v[i][0], v[i][1], True)

    return v, found_first_character, le


def check_full_match(
    pattern_attached: re.Pattern,
    pattern_nta_nti: re.Pattern,
    pattern_200_900: re.Pattern,
    pattern: re.Pattern,
    st: str,
):
    rm_numbers_pattern = re.compile(r'[0-9]')

    st = rm_numbers_pattern.sub('', st.strip())

    len_matches = sum(f.span()[1] - f.span()[0] for f in pattern_attached.finditer(st))
    new_s = pattern_attached.sub(lambda x: '#' * len(x.group()), st)

    for f in pattern_nta_nti.finditer(new_s):
        len_matches += f.span()[1] - f.span()[0]

    new_s = pattern_nta_nti.sub(lambda x: '#' * len(x.group()), new_s)

    for f in pattern_200_900.finditer(new_s):
        len_matches += f.span()[1] - f.span()[0]

    new_s = pattern_200_900.sub(lambda x: '#' * len(x.group()), new_s)

    for f in pattern.finditer(new_s):
        len_matches += f.span()[1] - f.span()[0]

    return 0 if len_matches != len(st) else 1


def num_letters_not_matched(
    pattern: re.Pattern,
    st: str,
    ord_dict: OrderedDict[str, int],
    duecento_novecento: List,
    letter_num_pattern: re.Pattern,
) -> str:
    if not st.isalpha():
        for g in separate_numeric_yield(
            pattern=pattern,
            st=st,
            ord_dict=ord_dict,
            duecento_novecento=duecento_novecento,
            letter_num_pattern=letter_num_pattern,
        ):
            yield g

    else:
        for ww in split_and_yield(
            pattern=pattern,
            st=st,
            ord_dict=ord_dict,
            duecento_novecento=duecento_novecento,
        ):
            yield ww


def read_yml(file_path: str):
    with open(file_path, 'r') as f:
        return safe_load(f)


def _pickled_objects_for_matching(file_path: str):
    config_pattern = read_yml(file_path)

    pickle_pattern_attached = unpickle_file(
        config_pattern['PATTERNS']['PATH']['pattern_attached'],
    )
    pickle_pattern_200_900 = unpickle_file(
        config_pattern['PATTERNS']['PATH']['pattern_200_900'],
    )
    pickle_pattern_nta_nti = unpickle_file(
        config_pattern['PATTERNS']['PATH']['pattern_nta_nti'],
    )
    pickle_main_pattern = unpickle_file(
        config_pattern['PATTERNS']['PATH']['main_pattern'],
    )

    return (
        pickle_pattern_attached,
        pickle_pattern_200_900,
        pickle_pattern_nta_nti,
        pickle_main_pattern,
    )


def _patterns_compiled(file_path: str):
    (
        pickle_pattern_attached,
        pickle_pattern_200_900,
        pickle_pattern_nta_nti,
        pickle_main_pattern,
    ) = _pickled_objects_for_matching(file_path)

    pattern_attached = re.compile(r'|'.join(pickle_pattern_attached))
    pattern_200_900 = re.compile(r'|'.join(pickle_pattern_200_900))
    pattern_nta_nti = re.compile(r'|'.join(pickle_pattern_nta_nti))
    letter_num_pattern = re.compile(
        read_yml(file_path)['PATTERNS']['PATTERN']['letter_num_pattern'],
    )
    pattern = re.compile(r'|'.join(pickle_main_pattern), flags=re.I)

    return (
        pattern_attached,
        pattern_200_900,
        pattern_nta_nti,
        letter_num_pattern,
        pattern,
    )


def find_pattern_user_text(file_path: str, phrase: str) -> bool:
    """
    Splits the phrase using whitespaces and returns True only if
    the pattern matches two consecutive words
    if in two consecutive words one is a digit and the other match the pattern
    :param file_path: path of the config file of the regex patterns
    :param phrase: phrase to extract and convert letters to number
    :return: bool
    """

    config_pattern = read_yml(file_path)
    pickle_main_pattern = unpickle_file(
        config_pattern['PATTERNS']['PATH']['main_pattern'],
    )
    pattern = re.compile(r'|'.join(pickle_main_pattern), flags=re.I)

    split = phrase.split()
    l = len(split)
    if l < 2:
        return True
    idx = 1

    for i in range(l):
        for v in range(idx, l):
            if pattern.search(split[i]) and pattern.search(split[v]):
                return True
            elif split[i].isdigit() and pattern.search(split[v]):
                return True
            elif split[v].isdigit() and pattern.search(split[i]):
                return True

            idx += 1
            break

    return False

    # pattern_attached, pattern_200_900, pattern_nta_nti, _, pattern = _patterns_compiled(file_path=file_path)
    #
    # for p in [pattern_attached, pattern, pattern_200_900, pattern_nta_nti]:
    #     if p.search(phrase):
    #         return True
    #
    # return False


def converted_numbers_joined(file_path: str, phrase: str, findall: bool = False) -> str:
    """
    Parse the phrase looking for letter to convert into numbers
    if there is a match (rules are described in the find_pattern_user_text function)
    returns the numbers joined as a string keeping the order in which the letters appear
    :param findall When set to True skips the rules described in the find_pattern_user_text function
    """
    if not findall:
        if not find_pattern_user_text(file_path=file_path, phrase=phrase):
            return ''

    _, duecento_novecento, _, d_ord = _pickled_objects_for_matching(file_path)

    (
        pattern_attached,
        pattern_200_900,
        pattern_nta_nti,
        letter_num_pattern,
        pattern,
    ) = _patterns_compiled(file_path)

    lista = []

    not_word_character_pattern = re.compile(r'[\\_\s\/-]*')

    for s in phrase.split():
        s = not_word_character_pattern.sub('', s)

        if not check_full_match(
            pattern_attached=pattern_attached,
            pattern_nta_nti=pattern_nta_nti,
            pattern_200_900=pattern_200_900,
            pattern=pattern,
            st=s,
        ):
            continue

        v, found_first_character, le = list_tuples_finditer(
            pattern_attached=pattern_attached,
            pattern_nta_nti=pattern_nta_nti,
            pattern_200_900=pattern_200_900,
            st=s,
        )

        if v:
            for i, k in enumerate(v, 1):
                new_s_2 = ''

                if k[2]:
                    lista.append(
                        letters_to_numbers(
                            pattern=pattern,
                            st=k[1],
                            ord_dict=d_ord,
                            duecento_novecento=duecento_novecento,
                        ),
                    )

                if i < le:
                    new_s_2 = s[k[0][1] : v[i][0][0]]
                else:
                    new_s_2 = s[k[0][1] :]

                if i == 1:
                    new_s_2 = s[0 : k[0][0]]

                #############################################################################################
                if found_first_character:
                    lista.append(
                        letters_to_numbers(
                            pattern=pattern,
                            st=k[1],
                            ord_dict=d_ord,
                            duecento_novecento=duecento_novecento,
                        ),
                    )

                    if i < le:
                        new_s_2 = s[k[0][1] : v[i][0][0]]

                ################################################################################################

                if i != 1:
                    if not k[2]:
                        lista.append(
                            letters_to_numbers(
                                pattern=pattern,
                                st=k[1],
                                ord_dict=d_ord,
                                duecento_novecento=duecento_novecento,
                            ),
                        )

                for g in num_letters_not_matched(
                    pattern=pattern,
                    st=new_s_2,
                    ord_dict=d_ord,
                    duecento_novecento=duecento_novecento,
                    letter_num_pattern=letter_num_pattern,
                ):
                    lista.append(g)

                if i == 1:
                    if not found_first_character:
                        lista.append(
                            letters_to_numbers(
                                pattern=pattern,
                                st=k[1],
                                ord_dict=d_ord,
                                duecento_novecento=duecento_novecento,
                            ),
                        )

                        if i < le:
                            new_s_2 = s[k[0][1] : v[i][0][0]]
                        else:
                            new_s_2 = s[k[0][1] :]

                        for g in num_letters_not_matched(
                            pattern=pattern,
                            st=new_s_2,
                            ord_dict=d_ord,
                            duecento_novecento=duecento_novecento,
                            letter_num_pattern=letter_num_pattern,
                        ):
                            lista.append(g)

                if i == le:
                    if new_s_2 != s[k[0][1] :]:
                        new_s_2 = s[k[0][1] :]
                        for g in num_letters_not_matched(
                            pattern=pattern,
                            st=new_s_2,
                            ord_dict=d_ord,
                            duecento_novecento=duecento_novecento,
                            letter_num_pattern=letter_num_pattern,
                        ):
                            lista.append(g)

                found_first_character = False

        else:
            for g in num_letters_not_matched(
                pattern=pattern,
                st=s,
                ord_dict=d_ord,
                duecento_novecento=duecento_novecento,
                letter_num_pattern=letter_num_pattern,
            ):
                lista.append(g)

    return ''.join(lista)
