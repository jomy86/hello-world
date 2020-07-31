
inputs="/home/jomymcet/test2_place.txt"

while IFS= read -r line
do
  python youtube_search.py "$line"
done < "$inputs"
