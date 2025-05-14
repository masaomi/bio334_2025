#!/usr/bin/env python

import random
import exercise_module

#random.seed(123)
pop_num = 50
seq_len = 50
generation = 300
mut_rate = 0.001
theta = 2.0*pop_num*mut_rate

#init populations
def init_pops():
  pops = []
  for i in range(0, pop_num):
    seq = ""
    for j in range(0, seq_len):
      nuc = ['A', 'T', 'G', 'C']
      seq += nuc[random.randint(0, 3)]
    pops.append(seq)
  return pops
pops = init_pops()
#print(pops)
#print(len(pops))

def mutation(seq, mut_rate):
  new_seq = ''
  for i in range(0, len(seq)):
    if random.random() < mut_rate:
      nuc = ['A', 'T', 'G', 'C']
      nuc = nuc[random.randint(0, 3)]
      new_seq += nuc 
    else:
      new_seq += seq[i]
  return new_seq

#print(pops[0])
#print(mutation(pops[0], mut_rate))
def random_select(pops):
  i = random.randint(0, len(pops)-1)
  seq = pops[i]
  return seq

#print(random_select(pops))
def next_pops(pops, mut_rate):
  new_pops = []
  seq = ''
  for i in range(0, len(pops)):
    seq = random_select(pops)
    seq = mutation(seq, mut_rate)
    new_pops.append(seq)
  return new_pops

#pops = next_pops(pops, mut_rate)
#print(pops)
#print(len(pops))


#main
f = open("result.dat","w")
print("Generation\ttheta\tseg_site_rate\tnuc_div\tTajimas_D")
print("Generation\ttheta\tseg_site_rate\tnuc_div\tTajimas_D", file=f)
for g in range(0, generation):
    #print g, "\t", theta, "\t", nuc_div(pops, seq_len), "\t", tajimas_d(pops), "\n";
    seg = exercise_module.count_seg_sites(pops)
    seg_rate = seg * 1.0 / seq_len
    nd = exercise_module.nucleotide_diversity(pops)
    td = exercise_module.tajimas_d(pops)
    print(g, "\t", theta, "\t", seg, "\t", nd, "\t", td) #python3
    print(g, "\t", theta, "\t", seg, "\t", nd, "\t", td, file=f)
    #print g, "\t", theta, "\t", seg_rate, "\t", nd, "\t", td
    pops = next_pops(pops, mut_rate); 
f.close()

f = open("final_pops.fa","w")
for i in range(0, len(pops)):
  seq = pops[i]
  f.write(">seq%d\n" % i)
  f.write(seq)
  f.write("\n")
f.close()
