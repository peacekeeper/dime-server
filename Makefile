GRADLE   = ./gradlew -q
TARGET   = build/libs/dime-server-0.1.0.jar
JAVADOC_DIR = build/docs/javadoc/
JAVADOC_WEB = shell.hiit.fi:/group/reknow/public_html/javadoc/dime-server/
SOURCES := $(shell find src/ -name '[A-Z]*.java' -or -name '*.html')

DOCKER_DB_DIR = ~/dime-db

LOCAL_PROPERTIES = config/application-local.properties
CLEAN_TMP_DIR = ~/.dime/tmp/cleandb
AUTOGEN_TMP_DIR = ~/.dime/tmp/autogen

all:	assemble

assemble:  $(TARGET)

$(TARGET): $(SOURCES)
	$(GRADLE) assemble

run:    $(TARGET)
	java -jar $(TARGET)

test:
	touch src/main/java/fi/hiit/dime/Application.java
	$(GRADLE) test
	@echo Now open ./build/reports/tests/index.html

clean:
	$(GRADLE) clean

doc: $(SOURCES)
	$(GRADLE) javadoc
	chmod -R a+r $(JAVADOC_DIR)
	rsync -var $(JAVADOC_DIR) $(JAVADOC_WEB)
	@echo
	@echo Now open ./build/docs/javadoc/index.html

docker: $(TARGET)
	docker build -t dime-server .

docker_db_dir:
	@echo Creating directory for mongodb ...
	mkdir $(DOCKER_DB_DIR)
	chmod 777 $(DOCKER_DB_DIR)

runDocker: docker docker_db_dir
	docker run -it -p 8080:8080 -v $(DOCKER_DB_DIR):/var/lib/mongodb dime-server

cleanDb:
	@echo Removing old temp dir $(CLEAN_TMP_DIR)
	rm -rf $(CLEAN_TMP_DIR)
	@echo Running tests to generate clean db
	SPRING_PROFILES_ACTIVE=cleandb $(MAKE) test

autogenDb:
	@echo Removing old temp dir $(AUTOGEN_TMP_DIR)
	rm -rf $(AUTOGEN_TMP_DIR)
	@echo Running tests to generate autogen db
	SPRING_PROFILES_ACTIVE=autogen $(MAKE) test

initSql: autogenDb
	rm -f src/main/resources/db/changelog/db.changelog-master.xml
	$(GRADLE) generateChangelog

updateSql: autogenDb cleanDb
	$(GRADLE) diffChangeLog
