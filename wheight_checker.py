import tensorflow as tf

# Load your saved model
model_path = "model_savings/dqn_from_dataset_Alex.keras"
model = tf.keras.models.load_model(model_path)

# Print weights of each layer
for layer in model.layers:
    print(f"Layer: {layer.name}")
    weights = layer.get_weights()  # List of numpy arrays: [weights, biases]
    if weights:
        for i, w in enumerate(weights):
            print(f"  Weight {i} shape: {w.shape}")
            print(w)
    else:
        print("  No weights in this layer.")
