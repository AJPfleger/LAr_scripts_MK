from __future__ import print_function
import argparse

from plotstyle import FCCStyle

import ROOT
ROOT.gROOT.SetBatch(ROOT.kTRUE)

def main():
    parser = argparse.ArgumentParser(description='Material Plotter')
    parser.add_argument('--fname', "-f", dest='fname', default="drift.root", type=str, help="name of file to read")
    parser.add_argument('--etaMax', "-m", dest='etaMax', default=1.19, type=float, help="maximum pseudorapidity")
    parser.add_argument('--etaBin', "-b", dest='etaBin', default=0.05, type=float, help="pseudorapidity bin width")
    args = parser.parse_args()

    f = ROOT.TFile.Open(args.fname, "read")
    tree = f.Get("materials")
    histDict = {}

    # go through the eta bins and fill the histograms in the histDict, skipping air
    # keys in the histDict are the material names
    for etaBin, entry in enumerate(tree):
        print(f"loop over tree: etaBin = {etaBin}")
        nMat = entry.nMaterials
        for i in range(nMat):
            print(f"loop over nMat, i = {i}")
            print(f"material = {entry.material.at(i)}")
            if entry.material.at(i) == "Air": continue
            if entry.material.at(i) not in histDict.keys():
                histDict[entry.material.at(i)] = {
                    "x0": ROOT.TH1F("", "", (int)(2 * args.etaMax / args.etaBin), -args.etaMax, args.etaMax),
                    "lambda": ROOT.TH1F("", "", (int)(2 * args.etaMax / args.etaBin), -args.etaMax, args.etaMax),
                    "depth": ROOT.TH1F("", "", (int)(2 * args.etaMax / args.etaBin), -args.etaMax, args.etaMax)
                }
            hs = histDict[entry.material.at(i)]
            hs["x0"].SetBinContent(etaBin+1, hs["x0"].GetBinContent(etaBin+1) + entry.nX0.at(i))
            hs["lambda"].SetBinContent(etaBin+1, hs["lambda"].GetBinContent(etaBin+1) + entry.nLambda.at(i))
            hs["depth"].SetBinContent(etaBin+1, hs["depth"].GetBinContent(etaBin+1) + entry.matDepth.at(i))
            
            print(hs)

    axis_titles = ["Number of X_{0}", "Number of #lambda", "Material depth [cm]"]
 
    # This loop does the drawing, sets the style and saves the pdf files
    for plot, title in zip(["x0", "lambda", "depth"], axis_titles):
        legend = ROOT.TLegend(.75, .75, .94, .94)
        legend.SetLineColor(0)
        ths = ROOT.THStack()
        print("histDict VOR dem 2. loop")
        print(histDict)
        for i, material in enumerate(histDict.keys()):
            linecolor = 1
            if i >= len(FCCStyle.fillcolors):
                i = i%len(FCCStyle.fillcolors)

            fillcolor = FCCStyle.fillcolors[i]
            histDict[material][plot].SetLineColor(linecolor)
            histDict[material][plot].SetFillColor(fillcolor)
            histDict[material][plot].SetLineWidth(1)
            histDict[material][plot].SetFillStyle(1001)
            
            print("histDict")
            print(histDict)
            print(histDict[material][plot])

            ths.Add(histDict[material][plot])
            legend.AddEntry(histDict[material][plot], material, "f")

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
        cv.Print(plot + ".pdf")
        cv.Print(plot + ".png")

        ths.GetXaxis().SetRangeUser(0, args.etaMax)
        cv.Print(plot + "pos.pdf")
        cv.Print(plot + "pos.png")

if __name__ == "__main__":
    FCCStyle.initialize()
    main()

