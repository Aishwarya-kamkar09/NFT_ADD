from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_dir = "data/certificates"

datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train_data = datagen.flow_from_directory(
    train_dir,
    target_size=(224,224),
    batch_size=32,
    class_mode='binary',
    subset='training'
)

print("CLASS MAPPING:", train_data.class_indices)