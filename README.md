# kanoodle-challenge
A collaborative Kanoodle puzzle challenge (solve, submit, analyze)

Date: 11:30 ET July 27, 2025

# 🧩 Kanoodle Challenge

Welcome to the **Kanoodle Challenge**. A collaborative puzzle-solving project where we use Python to solve custom Kanoodle-style puzzles.

---

## 💡 What Is This?

I'm building a solver for a puzzle made of Tetris-like pieces on an 11x5 board. The goal is to fit all the pieces in, no overlap, no gaps. Once it's working, other people can try to write their own solvers and submit their solutions too.

This is still in progress. Follow along, fork it, or join in later!

---

## 🔧 Current Setup

The repo has:

kanoodle-challenge/
├── puzzle/ # board size and official piece definitions
├── sample-solver/ # where I'm building my solver
├── submissions/ # other people will submit here later
├── heuristics/ # optional: analysis tools for submissions
└── README.md # you're here


---

## 🎯 What's Next?

- I'm going to build the logic in `sample-solver/solve.py`
- Once it works, I'll generate a `results.json` file
- Later, people can submit their own solutions under `/submissions/`

---

## 🧠 For Contributors (Soon)

1. Fork the repo
2. Copy `submissions/example-user/` to `submissions/your-name/` (if you want to build it you can as well)
3. Write your solver
4. Output your solution to `results.json`
5. Open a PR


---

## 🙌 Get Involved

Got ideas for how to solve this? Want to help with a visualizer, a solver strategy, or just watch it grow?  
Feel free to open an issue or DM me on IG: **[@judekansou]**



This is the rant:

My bad for the pictures but my housemate took the game and these are the only pictures I got of it.

So, my housemate got this game and as he was talking to me he randomly placed the pieces and ended up solving it. I tried and it took me a lot of time to no avail so I tired thinking of the heuristics of it and decided to code it up as I have not coded in like 3 months now. The code is meant to solve the pieces of which I have encoded in a matrix with every dot starting at (0,0)

The idea is to create a program that would solve it using a backtracking algorithm. The solution would then be printed out with a matrix of 5x11 with the pieces of every color being the letter in the matrix after the solution is done


This is as far as I got feel free to fork it and maybe if there is enough traction we can have a group chat.



