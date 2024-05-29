FROM maven:3.9.6-openjdk-17-jdk AS build
WORKDIR /apps
COPY pom.xml  .
RUN mvn clean package

FROM openjdk:17-jdk AS application
WORKDIR /apps
COPY --from=build /apps/target/snapchat.jar ./spc.jar
port 8080
CMD [ "java" , "-jar" , "spc.jar" ]