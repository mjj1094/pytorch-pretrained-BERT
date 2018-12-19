#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# from __future__ import absolute_import
# from __future__ import division
# from __future__ import print_function
# import tokenization

# orig_tokens = ["我们", "在", "上课",  "。"]
# labels      = ["NNP",  "NNP",      "POS", "NN"]
#
# ### Output
# bert_tokens = []
#
# # Token map will be an int -> int mapping between the `orig_tokens` index and
# # the `bert_tokens` index.
# orig_to_tok_map = []
# vocab_file='./data/Chinese_vocab.txt'
# tokenizer = tokenization.FullTokenizer(
#     vocab_file=vocab_file, do_lower_case=True)
#
# bert_tokens.append("[CLS]")
# for orig_token in orig_tokens:
#   orig_to_tok_map.append(len(bert_tokens))
#   bert_tokens.extend(tokenizer.tokenize(orig_token))
# bert_tokens.append("[SEP]")

import codecs
with codecs.open("./t/output.txt", 'w', encoding='utf-8', errors='ignore') as fw:
    fw.write("lalala\n"+'\n'+'\n')

