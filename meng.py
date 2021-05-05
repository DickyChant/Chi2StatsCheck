import sys
from math import exp,factorial,log
from numpy import random
import ROOT
from ROOT import TH1F, TCanvas, TRandom3, TF1, TFile

h1=TH1F('h1','h1',5000,0,50)
h2=TH1F('h2','h2',5000,0,50)

filein=TFile.Open('./sm_dy_bb.root')
hin=filein.Get('eta_b_run_01')
hg=filein.Get('test')
xs=hg.GetPointY(0)
yields=xs*1000000

b=[]
for i in range(1,11):
  b.append(hin.GetBinContent(i)*(yields/100000))

def ll(mu,b,n):
  lambdas=[]
  bins=[]
  for i in range(0,len(b)):
    lambda_temp=b[i]
    lambdas.append(lambda_temp)
    bins.append(n[i]*log(lambda_temp)-lambda_temp)

  a_out=0
  for i in range(0,len(b)):
    a_out=a_out+bins[i]

  return a_out

def main():
  gr1 = TRandom3()
  gr2 = TRandom3()
  gr3 = TRandom3()
  gr4 = TRandom3()
  gr5 = TRandom3()
  gr6 = TRandom3()
  gr7 = TRandom3()
  gr8 = TRandom3()
  gr9 = TRandom3()
  gr10 = TRandom3()
  gr1.SetSeed(0);
  gr2.SetSeed(0);
  gr3.SetSeed(0);
  gr4.SetSeed(0);
  gr5.SetSeed(0);
  gr6.SetSeed(0);
  gr7.SetSeed(0);
  gr8.SetSeed(0);
  gr9.SetSeed(0);
  gr10.SetSeed(0);
  for i in range(1,1000000):
    n=[]
    n1=gr1.Poisson(b[0])
    n2=gr2.Poisson(b[1])
    n3=gr3.Poisson(b[2])
    n4=gr4.Poisson(b[3])
    n5=gr5.Poisson(b[4])
    n6=gr6.Poisson(b[5])
    n7=gr7.Poisson(b[6])
    n8=gr8.Poisson(b[7])
    n9=gr9.Poisson(b[8])
    n10=gr10.Poisson(b[9])
    n.append(n1)
    n.append(n2)
    n.append(n3)
    n.append(n4)
    n.append(n5)
    n.append(n6)
    n.append(n7)
    n.append(n8)
    n.append(n9)
    n.append(n10)

    numerator=ll(0,n,n)
    denominator=ll(0,b,n)
    nll=2*(numerator-denominator)
    h1.Fill(nll)

  f1= TF1("f1","[0]*(x**4)*exp(-0.5*x)",0.,50)
  h1.Fit('chi2')
  c1=TCanvas('','',800,800)
  c1.cd()
  h1.Draw()
  f1.Draw('same')
  c1.SaveAs('aa.png')

if __name__ == "__main__":
  sys.exit(main())
 
