import pandas as pd

def getdf(fname, col_name, encoding=None, sep='\t'):
    if encoding is not None:
        df = pd.read_csv(fname, names=col_name, sep=sep, encoding=encoding)
    else:
        df = pd.read_csv(fname, names=col_name, sep=sep)
    df.dropna(inplace=True)
    return df

def fetch_file(file_name, start_line=0, end_line=0):
    if file_name == 'file2':
        df = getdf('file2.txt',
                    ['line_no', 'line_string'],
                    'utf-16')
    elif file_name == 'file4':
        df = getdf('file4.txt',
                    ['line_string'],
                    'utf-16')
    else:
        file_name = file_name + '.txt'
        df = getdf(file_name,
                    ['line_no', 'line_string'])

    if start_line == 0:
        file_lst = list(df['line_string'])
        text_str = '<br/>'.join(file_lst)
        return text_str
    else:
        if end_line == 0:
            end_line = df.shape[0]
        file_lst = df.iloc[start_line:end_line]['line_string'].to_list()
        text_str = '<br/>'.join(file_lst)
        return text_str