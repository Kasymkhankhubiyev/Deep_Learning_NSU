def multiclass_accuracy(prediction, ground_truth):
    """
    Computes metrics for multiclass classification

    Arguments:
    prediction, np array of int (num_samples) - model predictions
    ground_truth, np array of int (num_samples) - true labels

    Returns:
    accuracy - ratio of accurate predictions to total samples
    """

    tpn = 0
    for i in range(len(prediction)):
        if prediction[i] == ground_truth[i]:
            tpn += 1
    return tpn / len(prediction)
