#dcm4chee-scripts-backup

A set of scripts implementing an HSM that can be integrated with dcm4chee2.x
via the service "FileCopyHSMModule,type=Command."


##hsm_copy.py

This script is in charge of copying the tarball containing a series to the
backup location. It implements this by storing the tarball as an S3 object on
AWS.


##hsm_mmls.py

This script checks the status of a backup. It does so by querying AWS S3 for
the tarball, and verifying that it indeed exists. It returns “Archived” if yes,
and “Not_Found” if no (it’s not actually important what the latter is, as long
as it doesn’t match the regex of the “Pattern” field defined in the
FileCopyHSMModule bean).


##hsm_fetch.py

This script is in charge of fetching the archive from the back up location. It
gets called when a study is requested and the online copy exists in nearline,
or if the SynFileStatus service is configured to check the integrity of the tar
archive (ie: the “VerifyTar” is set to True).


## Sample usage

python hsm_copy.py --in-tar $PATH_TO_TARBALL --dest $AWS_S3_OBJECT_KEY
