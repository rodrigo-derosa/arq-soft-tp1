# Create image from node:10
FROM node:10
# Create directory in new image
RUN mkdir /app
# Set base dir. Now '.' means '/app'
WORKDIR /app
# Copy files
COPY app.js .
COPY package.json .
COPY package-lock.json .
# Install all requirements from package.json
RUN npm install
# How to run our app
ENTRYPOINT ["node", "app.js"]