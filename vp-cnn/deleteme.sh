#!/usr/bin/env bash

python main.py -emb-path ../w2v/ \
	-eval-on-test \
	-ensemble='vot' \
	-char-train-file=vp16.base.word.shuffled.35.txt \
	-word-train-file=vp16.base.word.shuffled.35.txt \
	-idx-file=vp16.base.shuffled.35.indices \
	-char-alt-file=separatedScored/elmo_src_para_joint.tsv \
	-word-alt-file=separatedScored/elmo_src_para_joint.tsv \
	-alt-prob=0.3 \
	-num-experts=2 \
	-char-test-file=test.tsv \
	-word-test-file=test.tsv \
	# -test-idx-file=test.labels \
	# -full-test-dialogues=vp17-cs.full.csv \
	-xfolds=0 \
	-epochs=1 \
	-word-batch-size=50 \
	-char-batch-size=200 \
	-char-kernel-num=100 \
	-word-kernel-num=200 \
	-char-embed-dim=100 -char-embed-dim=50 -word-kernel-sizes=1,2,3,4,5 \
	-char-kernel-sizes=1,2,3,4,5,6,7,8,9 -char-test-file=vp17.base.word.nonew.txt \
	-word-test-file=vp17.base.word.nonew.txt \
	-log-file=deleteme.log \
	-prediction-file-handle=deleteme.predictions.txt
