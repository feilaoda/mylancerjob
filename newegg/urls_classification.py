'''
Created on Oct 11, 2013

@author: lirans

This application receives as an input a file with URLs from one domain (i.e.: 'sears.com').
Each line contains a URL and the 'number of occurrences' of this URL in our data set.
The output of the application (to stdout) is the breakdown of all URLs in the input file to the URL classification rule that matched them.
If no rule was found then the URL will be under the 'unclassified' category.
This is an example of the output ('rule', 'num occurrences', 'percentege out of total occurrences')
list	10	29.4117647059%
search	9	26.4705882353%
product	8	23.5294117647%
unclassified	7	20.5882352941%

In addition the application writes all the unclassified URLs with their 'number of occurrences' to the output file.

Change the file names at the bootom of the file and the __import__ line to run on your domain
'''
import url_parser
import sys

mod = __import__('newegg', globals(), locals(), ['*'], -1)

# Count the number of occurrences each rule covers
def count_rule(url, counters, url_counter):    
    rule = url.get('rule')
    try:
        url_occurrence = int(url.get('count'))
    except:
        print "\nError in line: ", url_counter, ". couldn't convert ", url.get('count'), " to int"
        url_occurrence = 0
        pass
    
    if not rule: rule = 'unclassified'

    #print rule, " : ", url_occurrence
  
    if counters.get(rule):
        counters[rule] += url_occurrence
    else:
        counters[rule] = url_occurrence

    #print rule, " : ", counters[rule]
    return rule,url_occurrence

def process_line(line, counters, url_counter):
    parts = line.split('\t')

    url = parts[0].strip()

    if len(parts) == 2: 
        count = parts[1].strip()
    else:
        count = parts[len(parts)-1].strip()
        
#    if url_counter%1000 == 0:
#        print url, " : ", count

    parsed_url = dict()
    try:
        parsed_url = dict(url_parser.execute_rules(mod, url))
    except TypeError:
        print "\nError in line: ", url_counter, ". couldn't parse url ", url
        pass
        
    parsed_url['count'] = count      
    #print to_list(parsed_url)
    
    rule = count_rule(parsed_url, counters, url_counter)
    return rule

def to_list(url):
    ret = [url.get('action'), url.get('pn'), url.get('pid'), url.get('mid'), url.get('c1'), url.get('c1id'), 
            url.get('c2'), url.get('c2id'), url.get('search'), url.get('rule'), url.get('norm'), url.get('url')]
    #print ret
    return ret
    
def process_file(name, unclassified_urls):
    with open(name) as r, open(unclassified_urls, "w") as w:
        counters = dict()
        total_occurrences = 0
        url_counter = 0
        
        for line in r:
            rule = process_line(line, counters, url_counter)            

            if rule:
                if rule[0] == 'unclassified': w.write(line)
                #parts = line.split('\t')
                #to_print = rule[0] + '\t' + parts[0].strip() + '\t' + parts[1].strip() + '\n'
                #w.write(to_print)
                                        
                total_occurrences += rule[1]
                url_counter += 1

            if url_counter % 10000 == 0: sys.stdout.write('.')

        print('\n')
        for k, v in sorted(counters.items(), key=lambda x: (x[1],x[0]), reverse=True):
            print u'{0}\t{1}\t{2}%'.format(k, v, 100*float(v)/float(total_occurrences))
            

if __name__ == "__main__":
    process_file('newegg.txt', 'newegg_unclassified.txt')
    #process_file('../Domains/test.txt', '../Domains/test_unclassified.txt')    # Based on sears classification
