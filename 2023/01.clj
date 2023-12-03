(use '[clojure.string :only [last-index-of index-of]])

(defn get-digits [string] (filter #(Character/isDigit %) string))

(defn find-first-digit [string] (first (get-digits string)))
(defn find-last-digit [string] (last (get-digits string)))

(defn read-input []
  (loop [input (read-line) res []]
    (if (= "" input)
      res
      (recur (read-line) (conj res input)))))

(defn process_line_part1 [line_string]
  (+ (* 10 (Character/digit (find-first-digit line_string) 10))
     (Character/digit (find-last-digit line_string) 10)))

(def digit-strings ["1" "2" "3" "4" "5" "6" "7" "8" "9" "one" "two" "three"
                    "four" "five" "six" "seven" "eight" "nine"])

(defn get_first_indexes [string]
  (let [all-indices (map (fn [digit-string] [(index-of string digit-string) digit-string]) digit-strings)]
    (filter (fn [elt] (some? (first elt))) all-indices)))

(defn get_last_indexes [string]
  (let [all-indices (map (fn [digit-string] [(last-index-of string digit-string) digit-string]) digit-strings)]
    (filter (fn [elt] (some? (first elt))) all-indices)))

(defn get_first_digit [word]
  (second (apply min-key first (get_first_indexes word))))

(defn get_last_digit [word]
  (second (apply max-key first (get_last_indexes word))))

(defn digit_to_int [word]
  (case word
    "1" 1
    "2" 2
    "3" 3
    "4" 4
    "5" 5
    "6" 6
    "7" 7
    "8" 8
    "9" 9
    "one" 1
    "two" 2
    "three" 3
    "four" 4
    "five" 5
    "six" 6
    "seven" 7
    "eight" 8
    "nine" 9))

(defn process_line_part2 [line]
  (+ (* 10 (digit_to_int (get_first_digit line))) (digit_to_int (get_last_digit line))))

(def input (read-input))

(println (str "Part 1:" (reduce (fn [ans line] (+ ans (process_line_part1 line))) 0 input)))
(println (str "Part 2:" (reduce (fn [ans line] (+ ans (process_line_part2 line))) 0 input)))

