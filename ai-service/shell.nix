{
  pkgs ? import <nixpkgs> { },
}:
pkgs.mkShell {
  buildInputs = [
    pkgs.python3 # Ensure Python 3 is included
    pkgs.python3Packages.pip # Include pip for additional package management if needed
    pkgs.python3Packages.scikit-learn # Add scikit-learn
    pkgs.python3Packages.pandas # Add pandas
    pkgs.python3Packages.numpy # Add numpy
  ];

  # Optional: Set environment variables or scripts to run in the shell
  shellHook = ''
    echo "Python environment ready with scikit-learn, pandas, and numpy"
  '';
}
