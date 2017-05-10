#!/bin/bash -f

BASEDIR=$(dirname "$0")
LOCAL_SITE=$(python -m site --user-site)

# make Python local package dir if nonexist
echo ${LOCAL_SITE}
mkdir -p ${LOCAL_SITE}

# cp hook script into above dir
cp ${BASEDIR}/imphook_tf.py ${LOCAL_SITE}

# append hook import commands to 'sitecustomize.py'
# NOTE 'sitecustomize.py' will be loaded at Python start
cat ${BASEDIR}/sitecustomize.py.tmpl >> ${LOCAL_SITE}/sitecustomize.py
