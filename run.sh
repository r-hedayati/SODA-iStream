echo "------ Topology component running started ------"
xterm -title "Topology" -e "sh Topology/run.sh" &
echo "------ Network component running Finished ------"

echo "------ Server component running started ------"
xterm -title "Server" -e "sh Server/run.sh" &
echo "------ Server component running Finished ------"

echo "------ Client component running started ------"
xterm -title "Client" -e "sh Client/run.sh" &
echo "------ Client component running Finished ------"

# /bin/sh -ec 'cd frontend && echo frontend'
# /bin/sh -ec 'cd b
# xterm -title "App 1" -e "mycommand; mysecondcommand" 