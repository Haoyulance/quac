plt.style.use('ggplot')

train_f1_gb = [27.14,34.54,37.25,39.01,40.27,41.22,42.06,42.51,43.11,43.78,44.33,45.14,45.4,45.88,46.43,46.78,47.39,48.8,\
            49.41,49.61,49.83,50.11,51.22,51.66,51.8,51.8,52.17,52.58,53.05,52.83]
validation_f1_gb = [44.52,52.65,53.47,55.38,55.94,57.4,57.41,57.91,57.95,59.03,58.6,59.32,59.49,59.49,59.17,59.19,59.3,\
            59.74,59.63,59.54,59.61,59.63,60.04,59.59,59.76,59.73,59.39,59.71,59.71,59.56]

train_f1_glove = [25.45,29.94,32.76,34.79,35.94,36.91,37.85,38.53,39.22,40,40.55,40.81,41.59,41.86,42.48,42.9,43.4,43.9,44.4,\
            44.8,45.1,46.38,47.01,47.18,47.33,48.4,48.73,48.89,49.02,49.4]
validation_f1_glove = [37.1,39.7,47,49.07,50.51,51.34,52.25,53.69,53.52,52.3,52.7,54.71,54.45,54.83,55.06,55.10,55.59,54.98,55,\
                55.37,54.31,55.46,55.36,55.2,55.37,55.59,55.38,55.49,55.5,55.57]

train_f1_elmo = [27.87,34.6,36.85,38.28,39.21,39.96,40.68,41.22,41.83,42.23,42.88,43.22,44.42,44.82,45.07,45.39,45.8,46.03,46.33,\
                46.29,46.61,46.99,47.26,47.48,47.53,47.85,47.89,48.34,49.1,49.4]
validation_f1_elmo = [47.75,49.56,52.75,54.99,55.36,55.5,56.67,56.93,56.78,56.73,56.58,56.16,57.81,57.88,58.14,58.18,58.11,58.11,\
                        58.17,58.3,58.23,58.29,58.07,58.4,58.01,58.03,57.78,57.9,58.25,58.22]
max(train_f1_gb)
plt.figure(figsize=(15,4), dpi = 150)
plt.plot(range(1,31), validation_f1_elmo, '-.',color = 'darkturquoise', lw = 1,label = 'Elmo validation f1')
plt.plot(range(1,31), validation_f1_glove, '-.',color = 'steelblue', lw = 1,label = 'Baseline validation f1')
plt.plot(range(1,31), validation_f1_gb, '-.',color = 'purple', lw = 1,label = 'BERT validation f1')
plt.plot(range(1,31), train_f1_elmo, color = 'darkturquoise', lw = 1, label = 'Elmo training f1')
plt.plot(range(1,31), train_f1_glove, color = 'steelblue', lw = 1, label = 'Baseline training f1')
plt.plot(range(1,31), train_f1_gb, color = 'purple', lw = 1, label = 'BERT training f1')
plt.xticks(range(1,31))
plt.xlabel('Epoch', labelpad = 1)
plt.ylabel('F1 Score', labelpad = 1)
plt.legend(loc="lower right")
plt.savefig('Comparison', pad_inches = 0)
