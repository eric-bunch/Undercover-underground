----------------Google Foobar Challenge: Undercover Underground-------------------------------


The setup for this challenge is in the .txt file in this project. Unfortuanately, I did not 
finish this challenge in time. I had the two scripts in this project completed before the 
time was up, but the code parser kept giving me an enigmatic MemoryError. Both of the scripts 
ran fine on my own machine, even on cases with large numbers, but I guess google was wanting 
something even lighter.

I approached the problem as follows. I thought of the warrens connected by tunnels as a graph: 
vertices connected by edges (undirected). The condition that you can get from any warren to any 
other warren means that the graph must be connected. And in these graphs, there must be at most 
one edge connecting any two vertices. There is an implicit condition that no edge will start and 
end at the same vertex. All of these graphs have labelled verticies, so that we can tell them apart. 

The number of such graphs with N verticies and K edges we will denote by G(N, K). The generating 
function for G(N, K)/N! is given in the paper 'Enumeration of Labelled Graphs' by E. N. Gilbert, and 
can be found at https://oeis.org/A001187/a001187.pdf. 

I expound on the mathematics in a little more detail in the pdf contained in this project.
