#!/bin/bash
ts=(0 1 2 3)
tnames=("linear" "polynomial" "rbf" "sigmoid")
currDir=$(pwd)
traindata=$currDir/data/cross_validation/train_1
testdata=$currDir/data/cross_validation/test_1
svnTrain=$currDir/svm-train
svnPredict=$currDir/svm-predict
modelDir=$currDir/data/cross_validation/models
logFile=$modelDir/log
if [ -e $logFile ];then
  rm $logFile
fi
if [ ! -e $modelDir ];then
  mkdir -p $modelDir
fi
t=0
index=0
for t in ${ts[@]}:
do
  tname=${tnames[$index]}
  modelFile=$modelDir/model_${tname}
  predictFile=$modelDir/predict_${tname}
  echo $t $tname
  echo $t $tname >>$logFile
  echo "$svnTrain -t $t $traindata $modelFile >>$logFile"
  echo "$svnTrain -t $t $traindata $modelFile >>$logFile" >>$logFile
  $svnTrain -t $t $traindata $modelFile >>$logFile
  if [ $? -ne 0 ];then
	echo "error for $tname when train"
	echo "error for $tname when train" >>$logFile
	exit 1
  fi
  $svnPredict $testdata $modelFile $predictFile >>$logFile
  echo "$svnPredict $testdata $modelFile $predictFile >>$logFile"
  echo "$svnPredict $testdata $modelFile $predictFile >>$logFile" >>$logFile
  if [ $? -ne 0 ];then
	echo "error for $tname when predict"
	echo "error for $tname when predict" >>$logFile
	exit 1
  fi
  ((index++))
done

