#! /bin/bash
export PATH=$PATH:/root/.local/bin

##########################
# INIT
##########################

# the directory where the job stuff is
JOB_DIR='/grade/'
# the other directories
STUDENT_DIR=$JOB_DIR'student/'
TEST_DIR=$JOB_DIR'tests/'
OUT_DIR=$JOB_DIR'results/'

# where we will copy everything
MERGE_DIR=$JOB_DIR'run'
mkdir -p $MERGE_DIR  $OUT_DIR
cp $STUDENT_DIR* $MERGE_DIR
cp $TEST_DIR* $MERGE_DIR

##########################
# RUN
##########################

cd $MERGE_DIR

echo "[run] starting autograder"

# Run pytest and edulint to generate test results files
python3 -m pytest . --junit-xml=/grade/pytest_output.xml > /dev/null
python3 -m edulint -o no-flake8 --disable-explanations-update /grade/student/ > /grade/lint_output.txt

# run pltest.py to generate the results.json file from the results files
cd $JOB_DIR
python3 /autograder/pltest.py

if [ ! -s results.json ]
then
  # Let's attempt to keep everything from dying completely
  echo '{"succeeded": false, "score": 0.0, "message": "An unrecoverable error occured when testing your input. Contact course staff and have them check the logs for this submission."}' > results.json
fi


echo "[run] autograder completed"

# get the results from the file
cp $JOB_DIR/results.json '/grade/results/results.json'
echo "[run] copied results"
