from graphviz import Digraph

dot = Digraph(comment='Node Report', format='svg')

dot.node('@DEFAULT', '@DEFAULT')
dot.node('@INIT_MD', '@INIT_MD')
dot.node('@INIT_OPTG', '@INIT_OPTG')
dot.node('@INIT_MC', '@INIT_MC')
dot.node('@INIT_MD_', '@PRE-FORCES\n@FORCES\n@COORDS')
dot.node('@INIT_OPTG_', '@PRE-FORCES\n@FORCES\n@COORDS')

dot.edge('@DEFAULT', '@INIT_MD')
dot.edge('@DEFAULT', '@INIT_OPTG')
dot.edge('@DEFAULT', '@INIT_MC')
dot.edge('@INIT_MD', '@INIT_MD_')
dot.edge('@INIT_OPTG', '@INIT_OPTG_')

dot.render('../graphs/node-report.gv')
