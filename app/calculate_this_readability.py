

#%%
#md

"""
## Calculate Readability

This file calculates the FRE and NDC for all journals in the JournalSelection csv. All files are saved in ./data/abstracts as "lang.json".

Files are also concatenating into one big file (just for ease of process). The script "concatenatedLangDat_large_to_small.R" make these files even smaller.

Non preprocessed language files are also created and concatenated.

Main calculation functions are found in ./functions/readabilityFunctions.py

Treetagger needs to be installed with english tagger version.
"""

#%%
#md
"""
__One variable needs to be set in this file. repo_directory (next cell block) which points to the repo main directory__

"""
import os
import sys
#%%
#%%


import numpy as np
import pandas as pd
#import functions.dataminingfunctions as dmf
import functions.readabilityFunctions as rf
import treetaggerwrapper


#%%


journalInfo=pd.read_csv('./JournalSelection/JournalSelection.csv')




#%%
#md
"""
Define treetagger.
(Note, treetagger definitions can vary between windows and linux. Linux was used in the analysis. Using windows may see minor differences in parsing)
"""

#%%
#tagger = treetaggerwrapper.TreeTagger(TAGLANG='en')
def main(args=None):
    if args is None:
        args = sys.argv[1:]
    abstract = args[0]
    outdir = args[1]
    if outdir is not None:
        os.makedirs(outdir, exist_ok=False)
    tagger = treetaggerwrapper.TreeTagger(TAGLANG='en', TAGPARFILE="english.par")


    #%%
    #md
    """
    Calculate readability
    """
    #%%


    lDat = rf.analyze(
        abstract,
        [], #os.path.join(outdir, 'lang.json'),
        textType='abstracttext',
        columnList={'pubdate_year<>year','pmid','doi'},
        tagger=tagger)
    if lDat is None:
        lDat = pd.read_json(os.path.join(outdir,  'lang.json'))
    lDat = lDat.drop(columns=['doi', 'year', 'pmid'])
    for i, line in lDat.iterrows():
        pass
#        print(line)
    return line
#        i, index,doi,flesch,NDC,sylCount,sentenceCount,wordLength,wordCount,PercDiffWord,DiffWord_lst,pmid,year,journalID,articleID = line.split(",")
#        print(flesch)

# #%%
# #md
# """
# Calculate readability (without preprocessing of data)
# """
# #%%

# rf.analyze(abstract,
#            os.path.join(outdir, 'lang_noprepro.json'),
#            textType='abstracttext',
#            columnList={'pubdate_year<>year','pmid','strippedText','wordLength','wordCount','sentenceCount','sylCount','flesch','NDC','PercDiffWord','doi','DiffWord_lst'},
#            doPreprocessing=0,
#            tagger=tagger)




#%%
#md
"""
Concatenate the readability files
"""
#%%

# for n in [0]:
#     #Parameters needed (if left blank, get_./data/abstracts asks for response)
#     #What to search pubmed with

#     lDat=pd.read_json(os.path.join(outdir,  'lang.json'))
#     lDat.sort_index(inplace=True)
#     lDat.drop('strippedText',1,inplace=True)

#     newColumns = {'journalID','flesch','PercDifWord','sylCount','sentenceCount','wordCount','year','articleID'}
#     lDat['journalID']=np.zeros(len(lDat))+n
#     lDat['articleID']=lDat.index

#     if n==0:
#         cDat=lDat
#     else:
#         cDat=cDat.append(lDat)


# # Reset index and save
# cDat.reset_index(inplace=True)
# cDat.to_csv(os.path.join(outdir, "langdata.csv"))
# cDat.to_pickle(os.path.join(outdir, "langdata.pkl"))


# #%%
# #md
# """
# Concatenate the non-preprocessed readability files
# """
# #%%

# # Same as part for but for the unpreprocessed data
# for n in [0]:
#     #Parameters needed (if left blank, get_./data/abstracts asks for response)
#     #What to search pubmed with
#     lDat=pd.read_json(os.path.join(outdir, "lang_noprepro.json"))
#     lDat.sort_index(inplace=True)
#     lDat.drop('strippedText',1,inplace=True)

#     newColumns = {'journalID','flesch','PercDifWord','sylCount','sentenceCount','wordCount','year','articleID'}
#     lDat['journalID']=np.zeros(len(lDat))+n
#     lDat['articleID']=lDat.index

#     if n==0:
#         cDat=lDat
#     else:
#         cDat=cDat.append(lDat)

# # Reset index and save
# cDat.reset_index(inplace=True)
# cDat.to_csv(os.path.join(outdir, "langdata_noprepro.csv"))
# cDat.to_pickle(os.path.join(outdir, "langdata_noprepro.pkl"))
if __name__ == "__main__":
    main()
