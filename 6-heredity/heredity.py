import csv
import itertools
import sys

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    #print(f"people: {people}")
    #print(f"one_gene {one_gene}")
    #print(f"two_genes {two_genes}")
    #print(f"have_trait {have_trait}")
    
    total_prob = 1
    
    for person, details in people.items():
        
        name = person
        mother = people[name]["mother"]
        father = people[name]["father"]
        trait = people[name]["trait"]
        
        if name in one_gene:
            #print(f"{person} has one gene")
            num_gene = 1
            
        elif name in two_genes:
            #print(f"{person} has two gene")
            num_gene = 2
        
        else:
            #print(f"{person} has zero gene")
            num_gene = 0
        
        if name in have_trait:
            #print(f"{person} has trait")
            num_trait = True
        else:
            #print(f"{person} does not have trait")
            num_trait = False
            
        if mother == None:
            prob_genes = PROBS["gene"][num_gene]
            
        elif mother in one_gene:
            prob_genes_mother = 0.5
            
        elif mother in two_genes:
            prob_genes_mother = 1-PROBS["mutation"]
            
        else:
            prob_genes_mother = PROBS["mutation"]
        
        
        if father == None:
            prob_genes = PROBS["gene"][num_gene]
            
        elif father in one_gene:
            prob_genes_father = 0.5
            
        elif father in two_genes:
            prob_genes_father = 1-PROBS["mutation"]
        else:
            prob_genes_father = PROBS["mutation"]
            
            
            
        if mother == None or father == None:
            prob_genes =  PROBS["gene"][num_gene]
            
        elif num_gene == 0:
            prob_genes = (1 - prob_genes_mother) * (1 - prob_genes_father)
            
        elif num_gene == 1:
            prob_genes = (prob_genes_mother * (1 - prob_genes_father) )+ (prob_genes_father * (1 - prob_genes_mother))
        else:
            prob_genes = prob_genes_mother * prob_genes_father
            
        
        prob_trait_given_gene = PROBS["trait"][num_gene][num_trait]
        prob_genes_and_trait = prob_trait_given_gene * prob_genes
        total_prob *= prob_genes_and_trait
    
    #print(total_prob)
    return total_prob
            
        
    


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    for someone in probabilities:
        if someone in one_gene:
            probabilities[someone]["gene"][1] += p
        elif someone in two_genes:
            probabilities[someone]["gene"][2] += p
        else:
            probabilities[someone]["gene"][0] += p
        
        if someone in have_trait:
            probabilities[someone]["trait"][True] += p
        else:
            probabilities[someone]["trait"][False] += p
            


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    for person in probabilities:
        trait_true = probabilities[person]["trait"][True] 
        trait_false = probabilities[person]["trait"][False]
        sum = trait_true + trait_false
        new_true = trait_true / sum
        new_false = trait_false / sum
        
        probabilities[person]["trait"][True] = new_true
        probabilities[person]["trait"][False] = new_false
        
        gene_one = probabilities[person]["gene"][1]
        gene_two = probabilities[person]["gene"][2]
        gene_zero = probabilities[person]["gene"][0]
        sum = gene_one + gene_two + gene_zero
        new_one = gene_one / sum
        new_two = gene_two / sum
        new_zero = gene_zero / sum
        
        probabilities[person]["gene"][0] = new_zero
        probabilities[person]["gene"][1] = new_one
        probabilities[person]["gene"][2] = new_two



if __name__ == "__main__":
    main()
