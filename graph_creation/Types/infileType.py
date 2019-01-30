from enum import Enum

class InfileType(Enum):
    IN_ONTO_GO = 0
    IN_ONTO_DO = 1
    IN_ONTO_HPO = 2
    IN_ONTO_UBERON = 3

    IN_EDGE_CDT_PATH = 100
    IN_EDGE_DISGENET = 101
    IN_EDGE_GO = 102
    IN_EDGE_HPA = 103
    IN_EDGE_HPO_DIS = 104
    IN_EDGE_HPO_GENE = 105
    IN_EDGE_SIDER_IND = 106
    IN_EDGE_SIDER_SE = 107
    IN_EDGE_STITCH = 108
    IN_EDGE_STRING = 109
    IN_EDGE_DRUGCENTRAL_IND = 110
    IN_EDGE_BGEE_EXPR = 111
    IN_EDGE_BGEE_NO_EXPR = 112
    IN_EDGE_BGEE_OVEREXPR = 113
    IN_EDGE_BGEE_UNDEREXPR = 114
    IN_EDGE_STITCH_ACTIVATION = 115
    IN_EDGE_STITCH_BINDING = 116
    IN_EDGE_STITCH_CATALYSIS = 117
    IN_EDGE_STITCH_EXPRESSION = 118
    IN_EDGE_STITCH_INHIBITION = 119
    IN_EDGE_STITCH_PREDBIND = 120
    IN_EDGE_STITCH_REACTION = 121
    IN_EDGE_STITCH_BINDACT = 122
    IN_EDGE_STITCH_BINDINH = 123

    IN_EDGE_STRING_ACTIVATION = 125
    IN_EDGE_STRING_BINDING = 126
    IN_EDGE_STRING_CATALYSIS = 127
    IN_EDGE_STRING_EXPRESSION = 128
    IN_EDGE_STRING_INHIBITION = 129
    IN_EDGE_STRING_PTMOD = 130
    IN_EDGE_STRING_REACTION = 131
    IN_EDGE_STRING_BINDACT = 132
    IN_EDGE_STRING_BINDINH = 133

    IN_EDGE_DRUGCENTRAL_CONTRA_IND = 150

    IN_MAP_DISGENET = 200
    IN_MAP_STRING = 201
    IN_MAP_UNI_UNI_NCBI = 202
    IN_MAP_UNI_ENS_NCBI = 203
    IN_MAP_DRUGCENTRAL_PUBCHEM = 204

    IN_MAP_ONTO_DO_UMLS = 301
    IN_MAP_ONTO_DO_OMIM = 302
    IN_MAP_ONTO_HPO_UMLS = 303

    IN_MAP_ONTO_DO_ALT_ID =400
    IN_MAP_ONTO_GO_ALT_ID =401
    IN_MAP_ONTO_HPO_ALT_ID =402
