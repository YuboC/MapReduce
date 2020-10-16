# MapReduce

This repo provides two examples and a script to easily define and run mapper and reducer functions against Hadoop MapReduce.

Generally speaking, on the top level there are folders that must contain:

* mapper.py
* reducer.py
* sample directory with data to be copied in hdfs within docker container

__ENSURE THAT .py FILES HAVE `chmod +x` PERMISSIONS__
(This is hadoop requirement)

Of course, the idea is to add more folders that demonstrate different aggregations that can be achieved with MapReduce over different datasaets (that are available in the sample folder). The aspiration was to make something reusable quickly and cheaply.

## Usage

1. Download this repo
2. CD into this repo
3. Run the following

```
docker run \
  -v $(pwd):/usr/local/hadoop/py \
  -it sequenceiq/hadoop-docker:2.7.1 \
  /usr/local/hadoop/py/py_runner.sh basic_grep
```
(notice the **basic_grep** keyword at the end - corresponds to the folder **basic_grep**!)

expected output:

```
foo	6
quux	4
```
Another example:

```
docker run \
  -v $(pwd):/usr/local/hadoop/py \
  -it sequenceiq/hadoop-docker:2.7.1 \
  /usr/local/hadoop/py/py_runner.sh count
```
(notice the **count** keyword at the end  - corresponds to the folder **count**!)

expected output:

```
bar	0
foo	6
labs	0
quux	4
```
## *Question*: 
How would you update the simple grep above to manage __any__ type of search? (In this case it encodes the "f" / "x" searching inside the reducer function). So basically, what if I wanted to find all the words that have "oo" or all the words that start in "k" but end in "e" or all the words that have a single capital letter in them?

As you can imagine, the fix is not to hardcode all of these scenarios inside the map/reduce functions but instead, to come up with a more generic way to solve this.

- Answer to the Question:
 - Add a regular expression pattern argument

 - Pass the pattern as command line argument that can be read by `mapper.py` through `sys.argv[-1]`.

Use `re.search(pattern, word)` in `mapper.py`
use `argparse` package in python script to input the value that controlling the output

- Words that start wth `"f"` or end in `"x"`
```
docker run \
  -v $(pwd):/usr/local/hadoop/py \
  -it sequenceiq/hadoop-docker:2.7.1 \
  /usr/local/hadoop/py/py_runner.sh grep "^f|x$"
```
```
foo	6
quux	4
```
- Words that have `"oo"`
```
docker run \
  -v $(pwd):/usr/local/hadoop/py \
  -it sequenceiq/hadoop-docker:2.7.1 \
  /usr/local/hadoop/py/py_runner.sh grep "oo"
```
```
foo	6
```
- Other Patterns:

Words with only one capital `"^[a-z]*[A-Z][a-z]*$"`

Words that start with `"k"`, but end with `"e"` `"^k[a-zA-Z]*e$"`


(notice the **grep** keyword at the end - corresponds to the folder **grep**!)
