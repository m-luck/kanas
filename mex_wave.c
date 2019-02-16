void wave(char *y, char **target)
{
  /* you don't have to allocate memory, use target */
  /* y string is always null terminated */
  /* each string in target has length strlen(y) + 1 */
  int ind = 0;
  int stop = 0;
  for (unsigned int i = 0; i < strlen(y); i++) {
    while (y[i] == ' ') { // Inc i if space, skip over spaces
        i++;
        printf("Skipping...\n");
        if (i == strlen(y)) { // If space is last character, break all
          stop = 1;
          }
      }
    if (ind < strlen(y) && stop == 0) {
      unsigned int j = 0;
      for (j = 0; j < strlen(y); j++) { // Fill in target
        target[ind][j] = y[j];
//         printf("Setting to %c\n", y[j]);
      }
      target[ind][j+1] = "\0"; // Add null term for C to know to end string
//       printf("%s\n", target[ind]);
      target[ind][i] = toupper(y[i]); // To upper for the index 
      printf("%s\n",target[ind]);
      ind++; // Prepare for next target index
      }
    }
  return target;
}
