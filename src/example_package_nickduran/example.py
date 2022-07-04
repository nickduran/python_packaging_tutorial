def add_one(number):
    """
    Prepare transcripts for similarity analysis.

    Given individual .txt files of conversations,
    return a completely prepared dataframe of transcribed
    conversations for later ALIGN analysis, including: text
    cleaning, merging adjacent turns, spell-checking,
    tokenization, lemmatization, and part-of-speech tagging.
    The output serve as the input for later ALIGN
    analysis.

    Parameters
    ----------
    input_files : str (directory name) or list of str (file names)
        Raw files to be cleaned. Behavior governed by `input_as_directory`
        parameter as well.

    output_file_directory : str
        Name of directory where output for individual conversations will be
        saved.

    training_dictionary : str, optional (default: None)
        Specify whether to train the spell-checking dictionary using a
        provided file name (str) or the default Project
        Gutenberg corpus [http://www.gutenberg.org] (None).

    minwords : int, optional (2)
        Specify the minimum number of words in a turn. Any turns with fewer
        than the minimum number of words will be removed from the corpus.
        (Note: `minwords` must be equal to or greater than `maxngram` provided
        to `calculate_alignment()` and `calculate_baseline_alignment` in later
        steps.)

    use_filler_list : list of str, optional (default: None)
        Specify whether words should be filtered from all conversations using a
        list of filler words (list of str) or using regular expressions to
        filter out common filler words (None). Behavior governed by
        `filler_regex_and_list` parameter as well.

    filler_regex_and_list : boolean, optional (default: False)
        If providing a list to `use_filler_list` parameter, specify whether to
        use only the provided list (False) or to use both the provided list and
        the regular expression filter (True).

    add_stanford_tags : boolean, optional (default: False)
        Specify whether to return part-of-speech similarity scores based on
        Stanford POS tagger in addition to the Penn POS tagger (True) or to
        return only POS similarity scores from the Penn tagger (False). (Note:
        Including Stanford POS tags will lead to a significant increase in
        processing time.)

    stanford_pos_path : str, optional (default: None)
        If Stanford POS tagging is desired, specify local path to Stanford POS
        tagger.

    stanford_language_path : str, optional (default: None)
        If Stanford POS tagging is desired, specify local path to Stanford POS
        tagger for the desired language (str) or use the default English tagger
        (None).

    input_as_directory : boolean, optional (default: True)
        Specify whether the value passed to `input_files` parameter should
        be read as a directory (True) or a list of files to be processed
        (False).

    save_concatenated_dataframe : boolean, optional (default: True)
        Specify whether to save the individual conversation output data only
        as individual files in the `output_file_directory` (False) or to save
        the individual files as well as a single concatenated dataframe (True).

    Returns
    -------
    prepped_df : Pandas DataFrame
        A single concatenated dataframe of all transcripts, ready for
        processing with `calculate_alignment()` and
        `calculate_baseline_alignment()`.
    """
    return number + 1