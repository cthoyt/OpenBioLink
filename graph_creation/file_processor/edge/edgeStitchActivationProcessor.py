from graph_creation.file_processor.fileProcessor import FileProcessor
from graph_creation.Types.readerType import ReaderType
from graph_creation.Types.infileType import InfileType
from graph_creation.metadata_infile.edge.inMetaEdgeStitchActivation import InMetaEdgeStitchActivation


class EdgeStitchActivationProcessor(FileProcessor):

    IN_META_CLASS = InMetaEdgeStitchActivation

    def __init__(self):
        self.use_cols = self.IN_META_CLASS.USE_COLS
        super().__init__(self.use_cols, readerType=ReaderType.READER_EDGE_STITCH_ACTION,
                         infileType=InfileType.IN_EDGE_STITCH_ACTIVATION, mapping_sep=self.IN_META_CLASS.MAPPING_SEP)


    def individual_preprocessing(self, data):
        # only drug -> protein connections of single compounds (no merged)
        drug_protein = data.item_id_a.str.startswith('CIDs')
        mode = data['mode'] == 'activation'
        data = data[drug_protein & mode]
        self.stitch_to_pubchem_id(data,self.use_cols.index('item_id_a'))
        return data