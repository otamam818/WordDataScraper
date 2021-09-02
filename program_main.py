from program_headers import *

def main(): pass

def make_table(text, punctuation=False, to_return=False):
    """
        Makes a table of frequencies from the given text
        Input: An atricle of text
        Output: Either an exported file of .xlsx or .csv or the dataframe
    """

    # Remove punctuations if they are not wanted
    if not(punctuation):
        text = re.sub("\W+", " ", text)
    
    # Find the frequency of every word
    my_dict = {}
    for word in word_tokenize(text):
        # Make them all lowercase
        word_lcase = word.casefold()
        # Add it if it's not a stopword
        if not(word_lcase in STOPWORDS):
            if word_lcase in my_dict.keys():
                my_dict[word_lcase] += 1
            else:
                my_dict[word_lcase] = 1
    
    # Make an appropriate datatype to store in table format
    words_list = my_dict.keys()
    my_dict = {
        "Words" : words_list, 
        "Frequency" : [my_dict[i] for i in words_list]
    }
    
    # Create the dataframe, sorted by most-occuring words
    data = pd.DataFrame(my_dict)
    data = data.sort_values("Frequency", ascending=False)
    data = data.set_index("Words")

    # Either return or export it
    if to_return:
        return data
    else:
        # Ask the user their preferred file name and extension
        QApplication([])
        file_name, file_type = QFileDialog().getSaveFileName(None, 
            "Choose where to save", "", CSV_FILETYPE + ";;" + EXCEL_FILETYPE)
        
        # modify the file name to that it has the right extension
        ext_map = {CSV_FILETYPE: ".csv", EXCEL_FILETYPE: ".xlsx"}
        file_name = "".join(file_name.split('.')[:-1]) + ext_map[file_type]

        # Export the file accordingly
        {
            CSV_FILETYPE : data.to_csv,
            EXCEL_FILETYPE : data.to_excel
        }[file_type](file_name)

def make_bar_graph(text, num_items=10, file_name="data_bar_graph") -> None: 
    """Makes a bar graph of the frequencies of the given text"""
    
    # Get the data of repeats
    data = make_table(text, to_return=True).head(num_items)
    freq_dict = dict(data["Frequency"])

    # Set up the bar graph
    plt.style.use("seaborn")
    plt.figure(figsize=(25, 10))

    # Make it with different colors
    all_bars = plt.bar(range(num_items),freq_dict.values())
    for bar in all_bars:
        bar.set_color(choice(COLORS))

    # Add labels
    plt.title("Number of words in article", weight='bold', size='xx-large')
    plt.xlabel("Words", weight='bold')
    plt.ylabel("Number\nof\nrepeats", rotation=0, labelpad=50, weight='bold')
    plt.xticks(range(num_items), freq_dict.keys())

    # Save the figure
    plt.savefig(file_name+'.png', format='png')


def make_pie_chart(text): pass

def TEST_text():
    with open("my_text.txt", 'r') as my_file:
        return my_file.read()

if __name__=="__main__":
    main()
