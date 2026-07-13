import boto3

# Initialize AWS clients
s3 = boto3.client('s3')
polly = boto3.client('polly')

# Output bucket name
OUTPUT_BUCKET = "output-audio-bucket"

def lambda_handler(event, context):
    try:
        # Get uploaded file details
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        object_key = event['Records'][0]['s3']['object']['key']

        # Read text file from S3
        response = s3.get_object(Bucket=bucket_name, Key=object_key)
        text = response['Body'].read().decode('utf-8')

        # Convert text to speech
        polly_response = polly.synthesize_speech(
            Text=text,
            OutputFormat='mp3',
            VoiceId='Joanna'
        )

        # Save MP3 to output bucket
        output_key = object_key.replace('.txt', '.mp3')

        s3.put_object(
            Bucket=OUTPUT_BUCKET,
            Key=output_key,
            Body=polly_response['AudioStream'].read(),
            ContentType='audio/mpeg'
        )

        return {
            'statusCode': 200,
            'body': f'Audio file {output_key} created successfully.'
        }

    except Exception as e:
        print(str(e))
        return {
            'statusCode': 500,
            'body': str(e)
        }
