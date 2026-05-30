FROM python:3.11-slim

WORKDIR /app


# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip setuptools wheel && \
    pip install -r requirements.txt 

# Download spaCy English model
RUN python -m spacy download en_core_web_sm
RUN python -c "import stanza; stanza.download('sa')"

# Copy your app code
COPY . /app

# Add startup script
COPY ./scripts/prodstart.sh /prodstart.sh
RUN chmod +x /prodstart.sh

ENV PYTHONPATH=/app

EXPOSE 5001

CMD ["/prodstart.sh"]