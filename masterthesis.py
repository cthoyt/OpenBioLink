import argparse
import os

from graph_creation.graphCreator import GraphCreator
import cProfile
import graph_creation.graphCreationConfig as graphConfig
from train_test_set_creation import train_test_splitter as tts


def create_graph(args):
    working_dir = args.path
    graphConfig.DIRECTED = not args.undir
    graphConfig.QUALITY = args.qual
    graphConfig.INTERACTIVE_MODE = not args.no_interact
    graphConfig.SKIP_EXISTING_FILES = args.skip
    # graph_creator = GraphCreator("C:\\Users\\anna\\Desktop\\master")
    graph_creator = GraphCreator("test\\test_data")

    print("\n\n############### downloading files #################################")
    # graph_creator.download_db_files()

    print("\n\n############### creating graph input files #################################")
    # graph_creator.create_input_files()

    print("\n\n############### creating graph #################################")
    # graph_creator.create_graph()

def create_train_test_splits(args):
    if args.meta:
        pass
        #fixme read out triplets from path
    tts.random_edge_split(graph_path=args.edges, tn_graph_path=args.tn_edges, nodes_path=args.nodes,
                          val_frac=args.val_frac, test_frac=args.test_frac, crossval=args.crossval, folds=args.folds, meta_edge_triples=args.meta)
    #tts.random_edge_split('test\\test_data\\edges.csv', 'test\\test_data\\TN_edges.csv',  'test\\test_data\\nodes.csv', val_frac=0.2, test_frac = 0.2, crossval= None, folds = None)


def check_args_validity(args, parser):
    if not (args.g or args.s or args.c or args.t or args.e):
        parser.error("at least one action is required [-g, -s, -c, -t, -e]")
    if args.skip and args.no_interact is None:
        parser.error("--skip requires --no_interact")

def main(args_list=None):
    parser = argparse.ArgumentParser('Bio-Medical Graph Toolbox (BiMeG)')

    # Graph Creation
    parser.add_argument('-g', action='store_true', help='Generate Graph')
    parser.add_argument('--path', type=str, default= os.getcwd(),help='specify a working directory')
    parser.add_argument('--undir', action='store_true', help='Output-Graph should be undirectional (default = directional)')
    parser.add_argument('--qual', type=str, help= 'quality level od the output-graph, options = [hq, mq, lq], (default = None -> all entries are used)')
    parser.add_argument('--no_interact', action='store_true', help='Disables interactive mode - existing files will be replaced (default = interactive)')
    parser.add_argument('--skip', action='store_true', help='Existing files will be skipped - in combination with --no_interact (default = replace)')

    # Train- Test Split Generation
    parser.add_argument('-s', action='store_true', help='Generate Train-,Validation-, Test-Split')
    parser.add_argument('--edges', type=str, help='Path to edges.csv file (required with action -s')
    parser.add_argument('--tn_edges', type=str, help='Path to true_negatives_edges.csv file (required with action -s')
    parser.add_argument('--nodes', type=str, help='Path to nodes.csv file (required with action -s')
    parser.add_argument('--test_frac', type=float, default='0.2')
    parser.add_argument('--val_frac', type=float, default='0.2')
    parser.add_argument('--crossval')
    parser.add_argument('--folds')
    parser.add_argument('--meta', type=str, help='Path to meta_edge tripples (only required if meta-edges not known by system)')

    # Hyperparameter Optimization
    parser.add_argument('-c', action='store_true', help='Apply hyperparameter optimization via cross validation')

    # Training
    parser.add_argument('-t', action='store_true', help='Apply Training')

    # Testing and Evaluation
    parser.add_argument('-e', action='store_true', help='Apply Test and Evaluation')

    if args_list:
        args = parser.parse_args(args_list)
    else:
        args = parser.parse_args()

    check_args_validity(args, parser)

    if args.g:
        create_graph(args)

   # if args.s:
   #     create_train_test_splits()



if __name__ == '__main__':
    pr = cProfile.Profile()
    pr.enable()
    #main()
    base_dir = os.path.dirname(os.path.realpath(__file__))
    test_folder = os.path.join(base_dir, 'test')


    tts.random_edge_split(base_dir+'\\test\\test_data\\edges.csv',
                          base_dir+'\\test\\test_data\\TN_edges.csv',
                          base_dir+'\\test\\test_data\\nodes.csv',
                          val_frac=0.2, test_frac = 0.2, crossval= None, folds = None)

    pr.disable()
    pr.print_stats( sort="time")