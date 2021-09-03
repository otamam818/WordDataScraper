from program_headers import *

def main(): pass

def make_table(text, punctuation=False, to_return=False, qap=False, to_stem=False):
    """
        Makes a table of frequencies from the given text

        Parameters:
        @param: text: An atricle of text
        @param: punctuation: whether to include punctuation
        @param: to_return: whether the created dataframe should be returned 
            or exported
        @param: qap: whether QApplication has been called or not
        @param: to_stem: whether to include stemmed words
            
        Output: Either an exported file of .xlsx or .csv or the dataframe
    """

    # Remove punctuations if they are not wanted
    if not(punctuation):
        text = re.sub("\W+", " ", text)
    
    # Add a stemmer if it was asked for
    if to_stem:
        ps = PorterStemmer()

    # Find the frequency of every word
    my_dict = {}
    for word in word_tokenize(text):
        # Make them all lowercase
        word_lcase = word.casefold()
        # Add it if it's not a stopword
        if not(word_lcase in STOPWORDS):
            if to_stem:
                word_lcase = ps.stem(word_lcase)
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
        # Instantiate a QApplication if it has not been already
        if not(qap):
            QApplication([])
        # Ask the user their preferred file name and extension
        file_name, file_type = QFileDialog().getSaveFileName(None, 
            "Choose where to save", "", CSV_FILETYPE + ";;" + EXCEL_FILETYPE)

        # modify the file name to that it has the right extension
        ext_map = {CSV_FILETYPE: ".csv", EXCEL_FILETYPE: ".xlsx"}
        file_name = file_name.replace(".csv", '').replace(".xlsx", '')
        file_name += ext_map[file_type]

        # Export the file accordingly
        {
            CSV_FILETYPE : data.to_csv,
            EXCEL_FILETYPE : data.to_excel
        }[file_type](file_name)

def make_bar_graph(text, num_bars, qap=False,
                   punctuation=False, to_stem=False): 
    """
        Makes a bar graph of the frequencies of the given text

        Parameters:
        @param: text: An atricle of text
        @param: num_bars: the number of bars you want in the bar graph
        @param: qap: whether QApplication has been called or not
        @param: punctuation: whether to include punctuation
        @param: to_stem: whether to include stemmed words
    
        Output: An exported .png file
    """
    
    # Get the data of repeats
    data = make_table(
        text, punctuation, to_return=True, 
        qap=qap, to_stem=to_stem
    ).head(num_bars)
    freq_dict = dict(data["Frequency"])

    # Set up the bar graph
    plt.style.use("seaborn")
    plt.figure(figsize=(25, 10))

    # Make it with different colors
    all_bars = plt.bar(range(num_bars),freq_dict.values())
    for bar in all_bars:
        bar.set_color(choice(COLORS))

    # Add labels
    plt.title("Number of words in article", weight='bold', size='xx-large')
    plt.xlabel("Words", weight='bold')
    plt.ylabel("Number\nof\nrepeats", rotation=0, labelpad=50, weight='bold')
    plt.xticks(range(num_bars), freq_dict.keys())

    # Ask file name
    if not(qap):
        QApplication([])
    # Ask the user their preferred file name and extension
    file_name, file_type = QFileDialog().getSaveFileName(None, 
        "Choose where to save", "", PNG_FILETYPE)
    # modify the file name to that it has the right extension
    ext_map = {PNG_FILETYPE: ".png"}
    file_name = file_name.replace(".png", '') + ext_map[file_type]
    
    # Save the figure
    plt.savefig(file_name, format='png')

def TEST_text():
    with open("my_text.txt", 'r') as my_file:
        return my_file.read()

if __name__=="__main__":
    main()
