from enum import Enum

class ReaderType(Enum):
    READER_ONTO_GO = 0
    READER_ONTO_DO = 1
    READER_ONTO_HPO = 2
    READER_ONTO_UBERON = 3

    READER_EDGE_CDT_PATH = 100
    READER_EDGE_DISGENET = 101
    READER_EDGE_GO = 102
    READER_EDGE_HPA = 103
    READER_EDGE_HPO_DIS = 104
    READER_EDGE_HPO_GENE = 105
    READER_EDGE_SIDER_IND = 106
    READER_EDGE_SIDER_SE = 107
    READER_EDGE_STITCH = 108
    READER_EDGE_STRING = 109
    READER_EDGE_DRUGCENTRAL_IND = 110
    READER_EDGE_BGEE = 111
    READER_EDGE_BGEE_DIFF = 112
    READER_EDGE_STITCH_ACTION = 113
    READER_EDGE_STRING_ACTION = 114
    READER_EDGE_TN_HPO_DIS = 115

    READER_MAP_DISGENET = 10
    READER_MAP_STRING = 11
    READER_MAP_UNIPROT = 12
    READER_MAP_DRUGCENTRAL_PUBCHEM = 13