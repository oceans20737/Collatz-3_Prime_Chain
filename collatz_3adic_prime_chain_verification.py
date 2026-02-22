#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sympy import isprime

def get_next_n(n):
    rem = n % 3
    if rem == 0:
        return None
    elif rem == 1:
        return (4 * n - 1) // 3
    else:
        return (4 * n + 1) // 3

def generate_chain(start, max_length=20):
    chain = [start]
    print(f"Starting from: {start:,}")
    print(f"{start:,} → {'Prime' if isprime(start) else 'Not Prime'}")

    current = start
    for step in range(1, max_length):
        next_val = get_next_n(current)
        if next_val is None:
            print(f"Step {step}: Terminated (divisible by 3)")
            break

        prime_status = isprime(next_val)
        print(f"Step {step}: {next_val:,} → {'Prime' if prime_status else 'Not Prime'}")

        if not prime_status:
            break

        chain.append(next_val)
        current = next_val

    print(f"\nFinal Chain (Length {len(chain)}): {chain}")
    return chain

# Test
generate_chain(46000363)


# In[ ]:




