#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
from sympy import isprime

def get_next_n(n):
    rem = n % 3
    if rem == 0:
        return None
    elif rem == 1:
        return (4 * n - 1) // 3
    else:
        return (4 * n + 1) // 3

def run_exploration_show_all(start_range, end_range, min_display_length=6):
    print(f"--- 3-adic Exploration (Show All L ≥ {min_display_length}) ---")
    print(f"Range: {start_range:,} to {end_range:,}")
    start_time = time.time()

    all_long_chains = []

    print(f"[*] Level 1: Filtering primes...")
    candidates = [[i] for i in range(start_range, end_range) if isprime(i)]

    current_length = 1
    while candidates:
        next_level_candidates = []
        next_length = current_length + 1

        for chain in candidates:
            next_val = get_next_n(chain[-1])
            if next_val and isprime(next_val):
                new_chain = chain + [next_val]
                next_level_candidates.append(new_chain)
                if next_length >= min_display_length:
                    all_long_chains.append(new_chain)

        if not next_level_candidates:
            break

        candidates = next_level_candidates
        current_length = next_length
        print(f"    Found {len(candidates):,} chains of Length {current_length}!")

    end_time = time.time()
    print(f"\n--- All Chains of Length ≥ {min_display_length} ---")
    print(f"Total: {len(all_long_chains)} chains")
    for i, chain in enumerate(all_long_chains, 1):
        print(f"Chain {i} (Length {len(chain)}): {chain}")

    print(f"\nSearch Time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    run_exploration_show_all(start_range=2, end_range=100_000_000)


# In[ ]:




