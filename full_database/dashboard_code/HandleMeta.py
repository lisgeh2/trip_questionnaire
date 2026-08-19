import pyreadstat
import pickle
from contextlib import contextmanager
import sys
from pathlib import Path
from config import IN_GFS
from os.path import commonprefix

HERE = Path(__file__).parent


def get_value_labels(meta, variable_name):
    if IN_GFS:
        metatable = load_local_thing(path="MetaTable.pkl")

    if variable_name is None:
        return {}

    if IN_GFS:
        return metatable.columns[variable_name].item_value_labels

    else:
        value_labels = meta.variable_value_labels       # <-- fixed
        return value_labels.get(variable_name, {})      # <-- safe default


def get_column_label(meta, variable_name):
    if IN_GFS:
        metatable = load_local_thing(path="MetaTable.pkl")

    if variable_name is None:
        return {}

    if IN_GFS:
        return metatable.columns[variable_name].label

    else:
        col_labels = meta.column_names_to_labels        # <-- fixed
        return col_labels.get(variable_name, variable_name)  # fall back to var name


def get_group_label_and_single_label(meta, group_col_list):
    if IN_GFS:
        metatable = load_local_thing(path="MetaTable.pkl")

    if not IN_GFS:
        label_dict = {col: get_column_label(meta, col) for col in group_col_list}
        group_label = commonprefix(list(label_dict.values()))

        single_labels_dict = {}
        for col, label in label_dict.items():
            single_label = label.replace(group_label, "")
            single_labels_dict[col] = single_label

        return group_label, single_labels_dict

    elif IN_GFS:
        # sth like:
        label_dict = {col: get_column_label(meta, col) for col in group_col_list}
        group = metatable.columns[group_col_list[0]].group
        group_label = metatable.groups[group].value_label

        single_labels_dict = {}
        for col, label in label_dict.items():
            single_label = label.replace(group_label, "")
            single_labels_dict[col] = single_label

        return group_label, single_labels_dict
