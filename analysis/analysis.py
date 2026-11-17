"""Reproduce the counts and figures of the paper from the replication package.

Usage (from the repository root):
    python analysis/analysis.py            # prints counts, writes figures to analysis/figures/
Requires: pandas, matplotlib, numpy (see analysis/requirements.txt).
"""
import collections, os, sys
import pandas as pd
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
out = os.path.join(ROOT, 'analysis', 'figures'); os.makedirs(out, exist_ok=True)

s1 = pd.read_csv(os.path.join(ROOT, 'selection', 'stage1_screening.csv'), dtype=str).fillna('')
s2 = pd.read_csv(os.path.join(ROOT, 'selection', 'stage2_fulltext.csv'), dtype=str).fillna('')
ext = pd.read_csv(os.path.join(ROOT, 'extraction', 'extraction.csv'), dtype=str).fillna('')
cod = pd.read_csv(os.path.join(ROOT, 'analysis', 'coding.csv'), dtype=str).fillna('')

# ---- selection counts -------------------------------------------------------
print('Stage 1 (queue 1):', len(s1), 'records')
print(s1.stage1_decision.value_counts().to_string())
rej = s1[s1.stage1_decision == 'Rejected']
print('\nStage 1 exclusions by criterion and tag')
print(pd.crosstab(rej.stage1_criterion, rej.stage1_tag.replace('', '(no tag)'), margins=True).to_string())
print('\nStage 2 (full text):', len(s2), 'records')
print(s2.stage2_decision.value_counts().to_string())
print(s2[s2.stage2_decision == 'Rejected'].groupby(['stage2_criterion', 'stage2_tag']).size().to_string())
print('Accepted in Stage 2 by Stage 1 decision:')
print(pd.crosstab(s2.stage1_decision, s2.stage2_decision).to_string())

# ---- data of the included studies ------------------------------------------
df = ext.merge(cod, on='record_id', how='left')
df = df.rename(columns={'record_id': 'id', 'type_of_study': 'type', 'ai_technique': 'technique', 'ai_role': 'role',
    'target_disability': 'disability', 'validation_method': 'validation', 'disability_explicitly_stated': 'explicit',
    'ai_input': 'input', 'relation_to_rule_based_tools': 'relation', 'sdlc_phase': 'sdlc', 'issues_code': 'issues',
    'limitations_code': 'limits', 'ground_truth_code': 'gt', 'contribution_code': 'contrib', 'venue_type': 'venue'})
N = len(df)
print('\nIncluded studies:', N)
def counts(col, multi=True):
    c = collections.Counter()
    for v in df[col]:
        for x in (v.split(';') if multi else [v]): c[x.strip()] += 1
    return c
for col, multi in [('year', False), ('source', False), ('venue', False), ('type', True), ('context', False),
                   ('technique', True), ('role', True), ('input', True), ('relation', False), ('sdlc', True),
                   ('disability', True), ('explicit', False), ('validation', True), ('issues', True),
                   ('limits', True), ('gt', True), ('contrib', False)]:
    print(f'\n== {col}')
    for k, v in counts(col, multi).most_common(): print(f'  {k}: {v} ({100 * v / N:.0f}%)')
df['llm'] = df.technique.str.contains('LLM')
print('\nLLM by year'); print(pd.crosstab(df.year, df.llm).to_string())
gpt4o = df.models.str.contains(r'GPT-4o(?! mini)', regex=True) & ~df.models.str.startswith('Candidates')
print('Studies using GPT-4o (excluding GPT-4o mini only and candidate lists):', int(gpt4o.sum()), list(df[gpt4o].id))
print('Single technique family:', int((~df.technique.str.contains(';')).sum()))

# ---- figures ----------------------------------------------------------------
plt.rcParams.update({'font.family':'serif','font.size':7.5,'axes.edgecolor':'#8a8984','axes.linewidth':0.6,
  'xtick.color':'#52514e','ytick.color':'#0b0b0b','axes.labelcolor':'#52514e','pdf.fonttype':42,'svg.fonttype':'none'})
BLUE,ORANGE,INK,MUTED='#2a78d6','#eb6834','#0b0b0b','#52514e'
def save(fig,name):
    # metadata cleared so that the files carry no creation date or tool signature
    fig.savefig(os.path.join(out, f'{name}.pdf'), dpi=300, bbox_inches='tight',
                metadata={'Creator': None, 'Producer': None, 'CreationDate': None})
    fig.savefig(os.path.join(out, f'{name}.png'), dpi=300, bbox_inches='tight', metadata={'Software': None})
    plt.close(fig)
def multi(col):
    c=collections.Counter()
    for v in df[col]:
        for x in v.split(';'): c[x.strip()]+=1
    return c
# Fig: studies per year, LLM vs other
df['llm']=df.technique.str.contains('LLM')
years=['2022','2023','2024','2025','2026']
llm=[int(((df.year==y)&df.llm).sum()) for y in years]; oth=[int(((df.year==y)&~df.llm).sum()) for y in years]
fig,ax=plt.subplots(figsize=(3.3,1.9))
ax.bar(years,oth,color=ORANGE,width=0.6,label='No LLM (ML, DL, CV, NLP)',edgecolor='white',linewidth=1)
ax.bar(years,llm,bottom=oth,color=BLUE,width=0.6,label='LLM / generative AI',edgecolor='white',linewidth=1)
for i,(a,b) in enumerate(zip(oth,llm)):
    ax.text(i,a+b+0.3,str(a+b),ha='center',va='bottom',color=INK,fontsize=7)
ax.set_ylabel('Studies'); ax.set_ylim(0,17.5); ax.set_yticks([0,5,10,15])
ax.spines[['top','right']].set_visible(False); ax.yaxis.grid(True,color='#e4e3df',linewidth=0.5); ax.set_axisbelow(True)
ax.legend(frameon=False,loc='upper left',fontsize=6.5)
ax.set_xticks(range(5)); ax.set_xticklabels(['2022','2023','2024','2025','2026*'])
save(fig,'fig_year_llm')
# Fig: technique x role heatmap
techs=['LLM / Generative AI','Computer Vision','Machine Learning','Deep Learning','NLP']
roles=['Issue detection','Issue classification','Test generation','Support to the evaluation process','Recommendation of fixes','Automatic remediation']
rl=['Detec-\ntion','Classi-\nfication','Test\ngener.','Eval.\nsupport','Fix\nrecomm.','Auto.\nremed.']
M=[[0]*len(roles) for _ in techs]
for t,r in zip(df.technique,df.role):
    ts=[x.strip() for x in t.split(';')]; rs=[x.strip() for x in r.split(';')]
    for i,a in enumerate(techs):
        for j,b in enumerate(roles):
            if a in ts and b in rs: M[i][j]+=1
fig,ax=plt.subplots(figsize=(3.4,2.15))
from matplotlib.colors import LinearSegmentedColormap
cmap=LinearSegmentedColormap.from_list('b',['#eaf2fc','#2a78d6','#0d3c73'])
import numpy as np
A=np.array(M,dtype=float); Am=np.ma.masked_where(A==0,A)
ax.imshow(np.zeros_like(A),cmap=LinearSegmentedColormap.from_list('w',['#ffffff','#ffffff']),aspect='auto')
ax.imshow(Am,cmap=cmap,vmin=0,vmax=A.max(),aspect='auto')
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        v=int(A[i,j]); ax.text(j,i,str(v) if v else '\u2013',ha='center',va='center',fontsize=7,color=('white' if v>=8 else INK) if v else '#b5b4ae')
ax.set_xticks(range(len(roles))); ax.set_xticklabels(rl,fontsize=6.2)
ax.set_yticks(range(len(techs))); ax.set_yticklabels([f'{t} ({multi("technique")[t]})' for t in techs],fontsize=6.5)
ax.tick_params(length=0)
ax.set_xticks([x+0.5 for x in range(len(roles)-1)],minor=True); ax.set_yticks([y+0.5 for y in range(len(techs)-1)],minor=True)
ax.tick_params(which='minor',length=0); ax.grid(which='minor',color='white',linewidth=2)
[sp.set_visible(False) for sp in ax.spines.values()]
save(fig,'fig_technique_role')
# Fig: profile panels (horizontal bars)
panels=[('input','(a) Analyzed artifact (RQ1)',{'Source code/DOM':'Source code / DOM','Rendered UI/screenshot':'Rendered UI / screenshot','Images/alt text':'Images / alt text','Textual content':'Textual content','Runtime interaction':'Runtime interaction','GUI/accessibility tree':'GUI / accessibility tree','Not specified':'Not specified'}),
        ('relation','(b) Relation to rule-based tools (RQ1)',{'Hybrid (AI + rule-based tool)':'Hybrid (AI + rule-based)','AI only':'AI only','Compared with rule-based tools':'Compared with rule-based','Not specified':'Not specified'}),
        ('disability','(c) Target disability (RQ4.2)',{'Not specified':'Not specified','Visual impairment':'Visual','Multiple / Generic':'Multiple / generic','Cognitive impairment':'Cognitive','Motor impairment':'Motor'}),
        ('validation','(d) Validation method (RQ6)',{'Automated benchmark / Dataset':'Benchmark / dataset','Comparison with static tools':'Comparison with tools','Expert review':'Expert review','None / Proof of concept':'None / proof of concept','User study':'User study'})]
fig,axes=plt.subplots(2,2,figsize=(7.0,3.0))
for ax,(col,title,lab) in zip(axes.flat,panels):
    c=multi(col); items=[(lab[k],c.get(k,0)) for k in lab]
    items=[i for i in items]; ys=range(len(items))
    ax.barh(list(ys),[v for _,v in items],color=BLUE,height=0.62,edgecolor='white')
    for y,(_,v) in zip(ys,items): ax.text(v+0.4,y,f'{v}',va='center',fontsize=6.5,color=INK)
    ax.set_yticks(list(ys)); ax.set_yticklabels([k for k,_ in items],fontsize=6.6); ax.invert_yaxis()
    ax.set_xlim(0,N*0.72); ax.set_title(title,fontsize=7.5,loc='left',color=INK)
    ax.spines[['top','right']].set_visible(False); ax.tick_params(axis='y',length=0); ax.xaxis.grid(True,color='#e4e3df',linewidth=0.5); ax.set_axisbelow(True)
fig.tight_layout(w_pad=2.5,h_pad=1.2)
save(fig,'fig_profile')
print('Figures written to analysis/figures/')
