execfile("core.py")

import random

random.seed(2)
means = [0.1, 0.1,  0.8]
n_arms = len(means)
random.shuffle(means)
print means
arms = map(lambda (mu): BernoulliArm(mu), means)
print("Best arm is " + str(ind_max(means)))

algo = UCB1([], [])
algo.initialize(n_arms)
results = test_algorithm(algo, arms, 1, 500)

f = open("algorithms/ucb/ucb1_results.tsv", "w")

f.write("sim_nums \t times \t chosen_arms \t rewards \t cumulative_rewards \t average_rewards \n")


for i in range(len(results[0])):
  f.write("\t".join([str(results[j][i]) for j in range(len(results))]) + "\n")

f.close()
