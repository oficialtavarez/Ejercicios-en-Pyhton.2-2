def estrella():
    star = """
         .     *          .     
    .  *          .        .     *
          .        .          .        *
    *   .      * .    *    .      .
        .   *    .    *      .    *
     .   .    .    .    .    .    .
      .   .    \\|/     .       .   *
    .     .    -O-      .      .      .
          .    /|\\ .     .     .  .
     * .    .     .    .    .       *
        .     .     .     .    .   .
    .       .        .      .    .   *
          *           .     *       .
    """

    return star

def mensaje_agradecimiento():
    mensaje = """
    Querido profesor,
    
    Quería expresar mi más profundo agradecimiento por compartir tu conocimiento y sabiduría en algoritmos paralelos con nosotros. Me voy feliz, para mi fusite una inspiración y me motivaste a ampliar mi comprensión de este fascinante campo.
    
    Gracias por tu dedicación, paciencia y por guiarnos a través de este emocionante viaje de aprendizaje. 
 
    """
    print(mensaje + estrella())

mensaje_agradecimiento()
