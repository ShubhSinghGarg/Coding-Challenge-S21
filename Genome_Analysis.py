# to parse the data
from Bio import SeqIO
from Bio.Graphics import GenomeDiagram
#to present the data
from reportlab.lib import colors
from reportlab.lib.units import cm

color_set = [colors.green, colors.orange, colors.red, colors.purple, colors.cyan ]

record  = SeqIO.read("Genome.gb", "genbank")

gd_diagram = GenomeDiagram.Diagram("Tomato Curly Stunt Virus")
gd_track_for_features = gd_diagram.new_track(1, name="Annotated Features")
gd_feature_set = gd_track_for_features.new_set()


for feature in record.features:
    if feature.type != "gene":
        # dont consider the feature since not a gene.
        continue
    
    color = color_set[(len(gd_feature_set))]
    
    # the parameters for representation of each feature.
    gd_feature_set.add_feature(feature, sigil = "ARROW", arrowshaft_height = 0.5, color=color, label=True, label_size = 25, label_color = color)

# parameters for the diagram.
gd_diagram.draw(format="circular", circular=True, pagesize=(20*cm, 20*cm),
                start=0, end=len(record), circle_core=0.7)
gd_diagram.write("result_genome_circular.png", "PNG")

