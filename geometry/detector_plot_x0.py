import argparse

from plotstyle import FCCStyle

import ROOT

ROOT.gROOT.SetBatch(ROOT.kTRUE)

"""
Before running this, I created the following setup:

mkdir data
mkdir exports-detector-plots

Put all the root files in "data" and run this program from within "exports-detector-plots" as
python detector_plot_x0.py
"""


def parse_tree(tree, eta_max, eta_bin):
    """
    Takes a root tree and returns a dictionary.
    Combines all materials to a single one and ignore 'Air'.
    """
    # creat a dictionary, where we save x0 and co
    hist_dict_combined = {
        "x0": ROOT.TH1F("", "", (int)(2 * eta_max / eta_bin), -eta_max, eta_max),
        "lambda": ROOT.TH1F("", "", (int)(2 * eta_max / eta_bin), -eta_max, eta_max),
        "depth": ROOT.TH1F("", "", (int)(2 * eta_max / eta_bin), -eta_max, eta_max),
    }

    # go through the eta bins and fill the histograms in the histDict, skipping air
    for etaBin, entry in enumerate(tree):
        print(f"loop over tree: etaBin = {etaBin}")
        nMat = entry.nMaterials
        for i in range(nMat):
            print(f"loop over nMat, i = {i}")
            print(f"material = {entry.material.at(i)}")

            if entry.material.at(i) == "Air":
                continue

            hist_dict_combined["x0"].SetBinContent(
                etaBin + 1,
                hist_dict_combined["x0"].GetBinContent(etaBin + 1) + entry.nX0.at(i),
            )
            hist_dict_combined["lambda"].SetBinContent(
                etaBin + 1,
                hist_dict_combined["lambda"].GetBinContent(etaBin + 1)
                + entry.nLambda.at(i),
            )
            hist_dict_combined["depth"].SetBinContent(
                etaBin + 1,
                hist_dict_combined["depth"].GetBinContent(etaBin + 1)
                + entry.matDepth.at(i),
            )

            print(hist_dict_combined)

    return hist_dict_combined


def extract_material_from_all_root(file_list, eta_max, eta_bin):
    """
    Loops over all provided root files and extracts all info
    """

    hist_dict = {}

    for filename in file_list:
        f = ROOT.TFile.Open(filename, "read")
        tree = f.Get("materials")

        hist_dict[f] = parse_tree(tree, eta_max, eta_bin)

    return hist_dict


def main():
    parser = argparse.ArgumentParser(description="Material Plotter")
    parser.add_argument(
        "--fname",
        "-f",
        dest="fname",
        default="drift.root",
        type=str,
        help="name of file to read",
    )
    parser.add_argument(
        "--etaMax",
        "-m",
        dest="etaMax",
        default=1.19,
        type=float,
        help="maximum pseudorapidity",
    )
    parser.add_argument(
        "--etaBin",
        "-b",
        dest="etaBin",
        default=0.05,
        type=float,
        help="pseudorapidity bin width",
    )
    args = parser.parse_args()

    print(
        "WARNING the argument '--fname' is always ignored. Fall back to internal list."
    )

    file_list = (
        "../data/beaminstrum.root",
        "../data/beampipe.root",
        "../data/drift.root",
        "../data/homabs.root",
        "../data/LumiCal.root",
        "../data/vertex.root",
    )

    eta_max = args.etaMax
    eta_bin = args.etaBin

    hist_dict = extract_material_from_all_root(file_list, eta_max, eta_bin)

    axis_titles = ["Number of X_{0}", "Number of #lambda", "Material depth [cm]"]

    # This loop does the drawing, sets the style and saves the pdf files
    for plot, title in zip(["x0", "lambda", "depth"], axis_titles):
        legend = ROOT.TLegend(0.75, 0.75, 0.94, 0.94)
        legend.SetLineColor(0)
        ths = ROOT.THStack()
        print("histDict VOR dem 2. loop")
        print(hist_dict)
        for i, material in enumerate(hist_dict.keys()):
            linecolor = 1
            if i >= len(FCCStyle.fillcolors):
                i = i % len(FCCStyle.fillcolors)

            fillcolor = FCCStyle.fillcolors[i]
            hist_dict[material][plot].SetLineColor(linecolor)
            hist_dict[material][plot].SetFillColor(fillcolor)
            hist_dict[material][plot].SetLineWidth(1)
            hist_dict[material][plot].SetFillStyle(1001)

            print("histDict")
            # print(histDict)
            print(hist_dict[material][plot])

            ths.Add(hist_dict[material][plot])
            # legend.AddEntry(hist_dict[material][plot], material, "f")

        ths.SetMaximum(1.5 * ths.GetMaximum())
        print("print(ths.GetMaximum())")
        print(print(ths.GetMaximum()))
        cv = ROOT.TCanvas()
        ths.Draw()
        print("next line ths")
        print(ths.GetXaxis())
        ths.GetXaxis().SetTitle("#eta")
        print(ths.GetXaxis())
        ths.GetYaxis().SetTitle(title)

        legend.Draw()
        # cv.Print(plot + ".pdf")
        cv.Print(plot + "_mod.png")

        # ths.GetXaxis().SetRangeUser(0, args.etaMax)
        # cv.Print(plot + "pos.pdf")
        # cv.Print(plot + "pos.png")


if __name__ == "__main__":
    FCCStyle.initialize()
    main()
