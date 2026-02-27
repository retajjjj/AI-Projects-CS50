import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    
    model = dict()
    one_minus_d = 1 - damping_factor
    num_keys = len(corpus)
    prob_add = one_minus_d / num_keys
    links_in_page=[]
    
    
    for key, links in corpus.items():
        
        if key == page:
            num_links = len(links)
            if num_links == 0:
                num_links = num_keys
                
            prob_links = (1/num_links) * damping_factor
            for link in links:
                links_in_page.append(link)
            break
        
    for key, links in corpus.items():
        
        if key in links_in_page:
            model[key] = prob_links + prob_add
        else:
            model[key] = prob_add
        
    
    return model
        


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    sequence = []
    sample_probs=dict()
    probs=[]
    
    keys=[]
    for key in corpus:
        keys.append(key)
    
    random_start = random.choice(keys)
    probabilities = transition_model(corpus , random_start , damping_factor)
    
    for prob in probabilities.values():
        probs.append(int(n* prob))
          
        
    for _ in range(n):
        
        next = random.choices(keys, probs)
        next = next[0]
        sequence.append(next)
        probabilities = transition_model(corpus , next , damping_factor)
        probs.clear()
        
        for prob in probabilities.values():
            probs.append(int(n *prob))
        
    
    for key in corpus:
        count = sequence.count(key)
        sample_probs[key] = count/n
        
    
    return sample_probs
        
def num_links(corpus , page): 
   
    for key,links in corpus.items():
        if key == page and links:
            
            return len(links)
    
    
    return len(corpus)

def modified_corpus(corpus):
    keys=set()
    for key in corpus:
        keys.add(key)
        
    for key,links in corpus.items():
        if not links:
            corpus[key] = keys
            
    return corpus
            
    
def pr(corpus, page):
    pages_links_page=set()
    for key,links in corpus.items():
        for link in links:
            if link == page:
                pages_links_page.add(key)
    
    
       
    return pages_links_page
                
                
    
    
                 

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    
    diff = 1
    new_corpus = modified_corpus(corpus)
    
    initial_prob = 1/len(corpus)
    one_minus_d = 1 - damping_factor
    
    PR={}
    for key in corpus:
        PR[key] = initial_prob    
    
    while(diff > 0.001):
        diff= 0
    
        for key in corpus:
            pages_links_page = pr(new_corpus, key)

            prev=PR[key]
            
            sum=0
            for i in range (0 , len(pages_links_page)):
                sum +=  PR[list(pages_links_page)[i]] / num_links(new_corpus , list(pages_links_page)[i])
                
            PR[key] = one_minus_d/len(corpus) + (damping_factor * sum)
            diff = max( diff, abs(PR[key] - prev ))
            
        #print(f"greatest diff in this iteration: {diff}")
        
        #print(f"pr after {i} iteration {PR} ")
    
    return PR
    
    
    
    
        


if __name__ == "__main__":
    main()
