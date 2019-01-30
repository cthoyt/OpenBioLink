import os

import graph_creation.globalConstant as glob
from graph_creation.Types.qualityType import QualityType
from graph_creation.metadata_edge.edgeMetadata import EdgeMetadata
from graph_creation.metadata_infile import InMetaEdgeStitchActivation
from graph_creation.metadata_infile.mapping.inMetaMapString import InMetaMapString


class EdgeMetaDrugActivationGene(EdgeMetadata):
    LQ_CUTOFF = 0 #todo
    MQ_CUTOFF = 400
    HQ_CUTOFF = 700
    LQ_CUTOFF_TEXT = None
    MQ_CUTOFF_TEXT = None
    HQ_CUTOFF_TEXT = None

    def __init__(self, quality : QualityType= None):
        if quality is QualityType.HQ:
            cutoff_txt = EdgeMetaDrugActivationGene.HQ_CUTOFF_TEXT
            cutoff_num = EdgeMetaDrugActivationGene.HQ_CUTOFF
        elif quality is QualityType.MQ:
            cutoff_txt = EdgeMetaDrugActivationGene.MQ_CUTOFF_TEXT
            cutoff_num = EdgeMetaDrugActivationGene.MQ_CUTOFF
        elif quality is QualityType.LQ:
            cutoff_txt = EdgeMetaDrugActivationGene.LQ_CUTOFF_TEXT
            cutoff_num = EdgeMetaDrugActivationGene.LQ_CUTOFF
        else:
            cutoff_txt = None
            cutoff_num = None

        self.EdgesMetaClass = InMetaEdgeStitchActivation
        self.Map2MetaClass = InMetaMapString

        edges_file_path = os.path.join(glob.IN_FILE_PATH, self.EdgesMetaClass.CSV_NAME)
        mapping_file2 = os.path.join(glob.IN_FILE_PATH, self.Map2MetaClass.CSV_NAME)
        super().__init__(is_directional=True,
                         edges_file_path=edges_file_path,
                         colindex1=self.EdgesMetaClass.NODE1_COL, colindex2=self.EdgesMetaClass.NODE2_COL,
                         edgeType=self.EdgesMetaClass.EDGE_TYPE,
                         node1_type=self.EdgesMetaClass.NODE1_TYPE, node2_type=self.EdgesMetaClass.NODE2_TYPE,
                         colindex_qscore=self.EdgesMetaClass.QSCORE_COL, cutoff_num=cutoff_num, cutoff_txt=cutoff_txt,
                         mapping2_file=mapping_file2, map2_sourceindex=self.Map2MetaClass.SOURCE_COL, map2_targetindex=self.Map2MetaClass.TARGET_COL)
