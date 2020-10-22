install: download unzip welcome
    		
download:
	wget https://sravjti.tech/embedded-systems-study-group/assets/week2/code2.zip

unzip: 
	unzip code2.zip

welcome: main.o library.o string_add.o
	gcc main.o library.o string_add.o -o welcome

main.o: ./06/main.c
	gcc -c ./06/main.c -I./06/include

library.o: ./06/library.c
	gcc -c ./06/library.c -I./06/include

string_add.o: ./06/string_add.c
	gcc -c ./06/string_add.c -I./06/include

clean: 
	rm -rf *o welcome *.zip 06
