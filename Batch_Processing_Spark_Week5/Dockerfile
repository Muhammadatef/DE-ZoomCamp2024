FROM docker.io/bitnami/spark:3.3

# Set the environment variables for Python and Spark integration
ENV PYTHONPATH="${SPARK_HOME}/python/lib/py4j-0.10.9.5-src.zip:${SPARK_HOME}/python:${PYTHONPATH}"
ENV PATH="${HOME}/.local/bin:${PATH}"

# Switch to root user to install necessary packages
USER root
RUN apt-get update && \
    apt-get install -y python3-pip wget && \  
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*  # Clean up to reduce image size

# Copy the requirements.txt file into the container
# Install Python packages specified in requirements.txt
# If permissions errors occur, consider using the --user flag with pip install

# Switch back to the non-root user for security reasons
USER 1001

# Expose ports (if needed, e.g., for Jupyter)
# Spark UI port
EXPOSE 4040
# Jupyter Notebook port
EXPOSE 8888

# Set the working directory (optional)
WORKDIR /opt/bitnami/spark

# The CMD command can be used to run a specific application, for example, starting a Jupyter Notebook
# CMD ["jupyter", "notebook", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"] # Uncomment if Jupyter is needed
