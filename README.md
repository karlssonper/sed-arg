sed-arg
=======

user friendly python script that spits out a sed command

```
./sed-arg.py 
replace string:
> path/examples/myfile.jpg
replace path/examples/myfile.jpg with:
> path/examples/myfile.png
sed 's/path\/examples\/myfile.jpg/path\/examples\/myfile.png/g'
```